<template>
  <div :class="styles['professional-container']">
    <!-- Sidebar -->
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

    <!-- Main Content -->
    <main :class="styles['professional-main-content']">
      <!-- Header -->
      <div :class="styles['professional-header-row']">
        <div :class="styles['professional-top-bar']">
          <div :class="styles['professional-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <h1>Olá, {{ userName }}!</h1>
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

      <!-- Modal de Agendamento -->
      <div v-if="showScheduleModal" :class="styles['schedule-modal']">
        <div :class="styles['modal-overlay']" @click="closeModal"></div>
        <div :class="styles['modal-content']">
          <button :class="styles['close-button']" @click="closeModal">
            &times;
          </button>
          <div :class="styles['modal-header']">
            <h2>{{ selectedProfessional.name }}</h2>
            <p>{{ selectedProfessional.specialty }} - {{ selectedProfessional.crm }}</p>
            <div :class="styles['rating']">
              <span>4,8</span>
              <div :class="styles['stars']">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star-half-alt"></i>
              </div>
              <span>(122 avaliações)</span>
            </div>
          </div>
          <div :class="styles['calendar-container']">
            <div :class="styles['month-header']">
              <button @click="prevMonth">&lt;</button>
              <h3>{{ currentMonth }} {{ currentYear }}</h3>
              <button @click="nextMonth">&gt;</button>
            </div>
            <div :class="styles['days-grid']">
              <div v-for="day in daysOfWeek" :key="day" :class="styles['day-header']">
                {{ day }}
              </div>
              <div 
                v-for="day in calendarDays" 
                :key="day.date.toString()"
                :class="[
                  styles['day-cell'],
                  !day.isCurrentMonth ? styles['non-current-month'] : '',
                  day.isAvailable ? styles.available : styles.unavailable,
                  selectedDay && selectedDay.date.toString() === day.date.toString() ? styles.selected : ''
                ]"
                @click="selectDay(day)"
                :style="{
                  cursor: day.isCurrentMonth && day.isAvailable ? 'pointer' : 'not-allowed',
                  opacity: day.isCurrentMonth ? 1 : 0.5
                }"
              >
                {{ day.day }}
                <span v-if="day.isAvailable" :class="styles['available-indicator']"></span>
              </div>
            </div>
          </div>
          <div :class="styles['time-slots-container']">
            <h3>Horários Disponíveis</h3>
            <div :class="styles['time-slots-grid']">
              <button 
                v-for="time in availableTimes" 
                :key="time"
                :class="[
                  styles['time-slot'],
                  selectedTime === time ? styles.selected : ''
                ]"
                @click="selectTime(time)"
                :disabled="availableTimes.length === 0"
              >
                {{ time }}
              </button>
            </div>
          </div>
          <button 
            :class="styles['confirm-button']"
            :disabled="!selectedDay || !selectedTime"
            @click="confirmAppointment"
          >
            Confirmar Agendamento
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/ProfessionalView.module.css'
import api from '@/services/axios'

export default {
  data() {
    return {
      styles,
      userName: '',
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
<<<<<<< HEAD

      // Filtros e busca
      searchQuery: '',
      specialtyFilter: '',
      availabilityFilter: '',

      // Dados dos profissionais
=======
      searchQuery: '',
      specialtyFilter: '',
      availabilityFilter: '',
>>>>>>> 8b5e3b5f (Remover node_modules do repositório)
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
        }
      ],

      // Variáveis para o modal de agendamento
      showScheduleModal: false,
      selectedProfessional: null,
      selectedDay: null,
      selectedTime: null,
      currentDate: new Date(),
      availableTimes: []
    };
    }
  },
  computed: {
    specialties() {
      return [...new Set(this.professionals.map(p => p.specialty))]
    },
    filteredProfessionals() {
      return this.professionals.filter(professional => {
        const nameMatch = professional.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        const specialtyMatch = !this.specialtyFilter || professional.specialty === this.specialtyFilter
        let availabilityMatch = true

        if (this.availabilityFilter === 'available') {
          availabilityMatch = professional.available
        } else if (this.availabilityFilter === 'unavailable') {
          availabilityMatch = !professional.available
        }

        return nameMatch && specialtyMatch && availabilityMatch
      })
    },
    currentMonth() {
      return this.currentDate.toLocaleString('pt-BR', { month: 'long' })
    },
    currentYear() {
      return this.currentDate.getFullYear()
    },
    daysOfWeek() {
      return ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
    },
    calendarDays() {
      const year = this.currentDate.getFullYear()
      const month = this.currentDate.getMonth()
      const firstDay = new Date(year, month, 1)
      const lastDay = new Date(year, month + 1, 0)
      const prevMonthDays = firstDay.getDay()
      const nextMonthDays = 6 - lastDay.getDay()
      const days = []

      const prevMonthLastDay = new Date(year, month, 0).getDate()
      for (let i = prevMonthDays - 1; i >= 0; i--) {
        days.push({
          day: prevMonthLastDay - i,
          date: new Date(year, month - 1, prevMonthLastDay - i),
          isCurrentMonth: false,
          isAvailable: false
        })
      }

      for (let i = 1; i <= lastDay.getDate(); i++) {
        const date = new Date(year, month, i)
        days.push({
          day: i,
          date: date,
          isCurrentMonth: true,
          isAvailable: i % 2 !== 0,
          weekday: date.getDay()
        })
      }

      for (let i = 1; i <= nextMonthDays; i++) {
        days.push({
          day: i,
          date: new Date(year, month + 1, i),
          isCurrentMonth: false,
          isAvailable: false
        })
      }

      return days
    }
  },
  computed: {
    // Lista de especialidades únicas para o filtro
    specialties() {
      return [...new Set(this.professionals.map(p => p.specialty))];
    },

    // Profissionais filtrados
    filteredProfessionals() {
      return this.professionals.filter(professional => {
        const nameMatch = professional.name.toLowerCase().includes(this.searchQuery.toLowerCase());
        const specialtyMatch = !this.specialtyFilter || professional.specialty === this.specialtyFilter;
        let availabilityMatch = true;
        
        if (this.availabilityFilter === 'available') {
          availabilityMatch = professional.available;
        } else if (this.availabilityFilter === 'unavailable') {
          availabilityMatch = !professional.available;
        }

        return nameMatch && specialtyMatch && availabilityMatch;
      });
    },

    // Computeds para o calendário
    currentMonth() {
      return this.currentDate.toLocaleString('pt-BR', { month: 'long' });
    },
    currentYear() {
      return this.currentDate.getFullYear();
    },
    daysOfWeek() {
      return ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];
    },
    calendarDays() {
      const year = this.currentDate.getFullYear();
      const month = this.currentDate.getMonth();
      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      const prevMonthDays = firstDay.getDay();
      const nextMonthDays = 6 - lastDay.getDay();
      const days = [];

      // Dias do mês anterior
      const prevMonthLastDay = new Date(year, month, 0).getDate();
      for (let i = prevMonthDays - 1; i >= 0; i--) {
        days.push({
          day: prevMonthLastDay - i,
          date: new Date(year, month - 1, prevMonthLastDay - i),
          isCurrentMonth: false,
          isAvailable: false
        });
      }

      // Dias do mês atual (simulação: dias ímpares disponíveis)
      for (let i = 1; i <= lastDay.getDate(); i++) {
        const date = new Date(year, month, i);
        days.push({
          day: i,
          date: date,
          isCurrentMonth: true,
          isAvailable: i % 2 !== 0,
          weekday: date.getDay()
        });
      }

      // Dias do próximo mês
      for (let i = 1; i <= nextMonthDays; i++) {
        days.push({
          day: i,
          date: new Date(year, month + 1, i),
          isCurrentMonth: false,
          isAvailable: false
        });
      }

      return days;
    }
  },
  methods: {
    // Navegação do menu
    handleMenuClick(label) {
      this.activeMenu = label
      switch (label) {
        case 'INÍCIO':
          this.$router.push('/home')
          break
        case 'CONSULTAS':
          this.$router.push('/scheduling')
          break
        case 'PROFISSIONAIS':
          this.$router.push('/professional')
          break
        case 'PACIENTE':
          this.$router.push('/patient')
          break
        case 'MENSAGENS':
          this.$router.push('/message')
          break
        case 'CONFIGURAÇÕES':
          this.$router.push('/settings')
          break
        case 'SAIR':
          this.logout()
          break
      }
    },

    logout() {
      this.$router.push('/login');
    },

    // Controle do carrossel
    scrollCarousel(direction) {
      const carousel = this.$refs.carousel;
      const cardWidth = 280;
      const gap = 24;
      const scrollAmount = cardWidth + gap;
      carousel.scrollBy({ 
        left: direction === 'left' ? -scrollAmount : scrollAmount, 
        behavior: 'smooth' 
      });
    },

    // Métodos para o modal de agendamento
    scheduleAppointment(professional) {
      console.log('Agendando com:', professional.name);
      this.selectedProfessional = professional;
      this.showScheduleModal = true;
      this.selectedDay = null;
      this.selectedTime = null;
      this.currentDate = new Date();
      this.availableTimes = []; // Limpa os horários ao abrir novo agendamento
    },

    closeModal() {
      this.showScheduleModal = false;
    },

      this.$router.push('/login')
    },
    scrollCarousel(direction) {
      const carousel = this.$refs.carousel
      const cardWidth = 280
      const gap = 24
      const scrollAmount = cardWidth + gap
      carousel.scrollBy({ 
        left: direction === 'left' ? -scrollAmount : scrollAmount, 
        behavior: 'smooth' 
      })
    },
    scheduleAppointment(professional) {
      this.selectedProfessional = professional
      this.showScheduleModal = true
      this.selectedDay = null
      this.selectedTime = null
      this.currentDate = new Date()
      this.availableTimes = []
    },
    closeModal() {
      this.showScheduleModal = false
    },
    prevMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() - 1,
        1
      );
      this.selectedDay = null;
      this.selectedTime = null;
      this.availableTimes = [];
    },

      )
      this.selectedDay = null
      this.selectedTime = null
      this.availableTimes = []
    },
    nextMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() + 1,
        1
      );
      this.selectedDay = null;
      this.selectedTime = null;
      this.availableTimes = [];
    },

    selectDay(day) {
      if (day.isCurrentMonth && day.isAvailable) {
        this.selectedDay = day;
        this.updateAvailableTimes(day);
      } else if (day.isCurrentMonth && !day.isAvailable) {
        this.selectedDay = null;
        this.selectedTime = null;
        this.availableTimes = [];
        alert('Este dia não possui horários disponíveis para agendamento');
      }
    },

    updateAvailableTimes(day) {
      if (!day || !day.isAvailable) {
        this.availableTimes = [];
        return;
      }
      
      // Simulação de horários disponíveis
      if (day.day % 2 === 0) { // Dias pares - menos horários
        this.availableTimes = ['09:00', '11:00', '15:00'];
      } else { // Dias ímpares - mais horários
        this.availableTimes = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00', '16:00'];
      }
    },

    selectTime(time) {
      this.selectedTime = time;
    },

    confirmAppointment() {
      if (this.selectedDay && this.selectedTime) {
        const formattedDate = this.selectedDay.date.toLocaleDateString('pt-BR');
        alert(`Consulta agendada com ${this.selectedProfessional.name}\nData: ${formattedDate}\nHorário: ${this.selectedTime}`);
        this.closeModal();
      }
    }
  }
};
</script>
      )
      this.selectedDay = null
      this.selectedTime = null
      this.availableTimes = []
    },
    selectDay(day) {
      if (day.isCurrentMonth && day.isAvailable) {
        this.selectedDay = day
        this.updateAvailableTimes(day)
      } else if (day.isCurrentMonth && !day.isAvailable) {
        this.selectedDay = null
        this.selectedTime = null
        this.availableTimes = []
        alert('Este dia não possui horários disponíveis para agendamento')
      }
    },
    updateAvailableTimes(day) {
      if (!day || !day.isAvailable) {
        this.availableTimes = []
        return
      }
      if (day.day % 2 === 0) {
        this.availableTimes = ['09:00', '11:00', '15:00']
      } else {
        this.availableTimes = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
      }
    },
    selectTime(time) {
      this.selectedTime = time
    },
    confirmAppointment() {
      if (this.selectedDay && this.selectedTime) {
        const formattedDate = this.selectedDay.date.toLocaleDateString('pt-BR')
        alert(`Consulta agendada com ${this.selectedProfessional.name}\nData: ${formattedDate}\nHorário: ${this.selectedTime}`)
        this.closeModal()
      }
    }
  },
  async created() {
    try {
      const response = await api.get('/auth/me')
      this.userName = response.data.nome
    } catch (error) {
      console.error('Erro ao carregar o nome do usuário:', error)
    }
  }
}
</script>
