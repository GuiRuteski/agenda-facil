<template>
  <div :class="styles['professional-container']">
    <!-- Layout principal -->
    <aside :class="styles['professional-sidebar']">
      <div :class="styles['professional-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['professional-logo']" 
        />
      </div>
      <ul :class="styles['professional-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['professional-menu-item'], activeMenu === item.label ? styles['professional-active-menu'] : '']"
          role="button"
          tabindex="0"
          @click="handleMenuClick(item.label)"
        >
          <i :class="[item.icon]" style="margin-right: 10px;"></i>
          {{ item.label }}
        </li>
      </ul>
    </aside>

    <main :class="styles['professional-main-content']">
      <!-- Cabeçalho -->
      <div :class="styles['professional-header-row']">
        <div :class="styles['professional-top-bar']">
          <div :class="styles['professional-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['professional-user-underline-box']">
              <div :class="[styles['professional-user-underline'], styles.short]"></div>
              <div :class="[styles['professional-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['professional-user-photo']" 
          />
        </div>     
      </div>

      <!-- Filtros -->
      <div :class="styles['professional-filters']">
        <div :class="styles['professional-search-container']">
          <i class="fas fa-search" :class="styles['professional-search-icon']"></i>
          <input 
            type="text" 
            placeholder="Buscar profissional..." 
            v-model="searchQuery"
            :class="styles['professional-search-input']"
          >
        </div>

        <div :class="styles['professional-filters-row']">
          <div :class="styles['professional-filter-group']">
            <select v-model="specialtyFilter" :class="styles['professional-filter-select']">
              <option value="">Todas especialidades</option>
              <option v-for="spec in specialties" :value="spec" :key="spec">{{ spec }}</option>
            </select>
          </div>
          <div :class="styles['professional-filter-group']">
            <select v-model="availabilityFilter" :class="styles['professional-filter-select']">
              <option value="">Todos os status</option>
              <option value="available">Disponível</option>
              <option value="unavailable">Indisponível</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Carrossel de Profissionais -->
      <div :class="styles['professional-carousel-wrapper']">
        <button 
          :class="styles['carousel-arrow']" 
          @click="scrollCarousel('left')"
          aria-label="Anterior"
        >
          ←
        </button>
        <div :class="styles['professional-carousel']" ref="carousel">
          <div :class="styles['carousel-track']">
            <div 
              v-for="professional in filteredProfessionals" 
              :key="professional.id"
              :class="styles['professional-card']"
            >
              <div :class="styles['card-header']">
                <img 
                  :src="professional.photo || require('../assets/Doctor.jpg')" 
                  :class="styles['professional-photo']"
                  alt="Foto do profissional"
                />
                <div :class="styles['professional-info']">
                  <h3>{{ professional.name }}</h3>
                  <p>{{ professional.specialty }}</p>
                  <p>CRM: {{ professional.crm }}</p>
                </div>
              </div>
              <div :class="styles['professional-card-status']">
                <span :class="[
                  styles['professional-status-badge'],
                  professional.available ? styles.available : styles.unavailable
                ]">
                  {{ professional.available ? 'Disponível' : professional.unavailableReason }}
                </span>
              </div>
              <button 
                :class="[
                  styles['professional-schedule-button'],
                  professional.available ? '' : styles.disabled
                ]"
                :disabled="!professional.available"
                @click="scheduleAppointment(professional)"
              >
                Agendar Consulta
              </button>
            </div>
          </div>
        </div>
        <button 
          :class="styles['carousel-arrow']" 
          @click="scrollCarousel('right')"
          aria-label="Próximo"
        >
          →
        </button>
      </div>
    </main>
  </div>
</template>



<script>
import styles from '@/assets/css/ProfessionalView.module.css';

export default {
  data() {
    return {
      styles,
      userName: 'Marcos',
      userPhoto: require('../assets/User.jpg'),
      menuItems: [
        { label: 'INÍCIO', icon: 'fas fa-home' },
        { label: 'CONSULTAS', icon: 'fas fa-calendar-check' },
        { label: 'PROFISSIONAIS', icon: 'fas fa-user-md' },
        { label: 'PACIENTE', icon: 'fas fa-user' },
        { label: 'MENSAGENS', icon: 'fas fa-comments' },
        { label: 'CONFIGURAÇÕES', icon: 'fas fa-cog' },
        { label: 'SAIR', icon: 'fas fa-sign-out-alt' }
      ],
      activeMenu: 'PROFISSIONAIS',

      // Filtros e busca
      searchQuery: '',
      specialtyFilter: '',
      availabilityFilter: '',

      // Dados dos profissionais (simulados - substituir por chamada API)
      professionals: [
        {
          id: 1,
          name: 'Dr. João Pereira',
          specialty: 'Cardiologista',
          crm: 'CRM 123456-SP',
          photo: require('../assets/Doctor.jpg'),
          available: true
        },
        {
          id: 2,
          name: 'Dra. Ana Oliveira',
          specialty: 'Ortopedista',
          crm: 'CRM 987654-RJ',
          photo: require('../assets/Doctor.jpg'),
          available: true
        },
        {
          id: 3,
          name: 'Dr. Rubens Silva',
          specialty: 'Pediatra',
          crm: 'CRM 456321-MG',
          photo: require('../assets/Doctor.jpg'),
          available: false,
          unavailableReason: 'De férias'
        },
        {
          id: 4,
          name: 'Dra. Camila Ferreira',
          specialty: 'Neurologista',
          crm: 'CRM 654789-RS',
          photo: require('../assets/Doctor.jpg'),
          available: true
        },
        {
          id: 5,
          name: 'Teste de carrossel',
          specialty: 'Neurologista',
          crm: 'CRM 654789-RS',
          photo: require('../assets/Doctor.jpg'),
          available: true
        }
      ]
    };
  },
  computed: {
    // Lista de especialidades únicas para o filtro
    specialties() {
      return [...new Set(this.professionals.map(p => p.specialty))];
    },

    // Profissionais filtrados
    filteredProfessionals() {
      return this.professionals.filter(professional => {
        // Filtro por nome
        const nameMatch = professional.name.toLowerCase().includes(this.searchQuery.toLowerCase());

        // Filtro por especialidade
        const specialtyMatch = !this.specialtyFilter ||
          professional.specialty === this.specialtyFilter;

        // Filtro por disponibilidade
        let availabilityMatch = true;
        if (this.availabilityFilter === 'available') {
          availabilityMatch = professional.available;
        } else if (this.availabilityFilter === 'unavailable') {
          availabilityMatch = !professional.available;
        }

        return nameMatch && specialtyMatch && availabilityMatch;
      });
    }
  },
  methods: {
    handleMenuClick(label) {
      this.activeMenu = label;
      switch (label) {
        case 'INÍCIO':
          this.$router.push('/home');
          break;
        case 'CONSULTAS':
          this.$router.push('/scheduling');
          break;
        case 'PROFISSIONAIS':
          this.$router.push('/professional');
          break;
        case 'PACIENTE':
          this.$router.push('/patient');
          break;
        case 'MENSAGENS':
          this.$router.push('/message');
          break;
        case 'CONFIGURAÇÕES':
          this.$router.push('/settings');
          break;
        case 'SAIR':
          this.logout();
          break;
      }
    },
    logout() {
      this.$router.push('/login');
    },
    scrollCarousel(direction) {
      const carousel = this.$refs.carousel;
      const cardWidth = 280; // mesmo valor do seu CSS (max-width/min-width do card)
      const gap = 24; // mesmo valor do gap no CSS (1.5rem = 24px)
      const scrollAmount = cardWidth + gap;
      if (direction === 'left') {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
      }
    },
    scheduleAppointment(professional) {
      // Implemente aqui a lógica de agendamento
      alert(`Agendar consulta com ${professional.name}`);
    }
  }
};
</script>
