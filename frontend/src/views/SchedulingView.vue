<template>
  <div :class="styles['scheduling-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['scheduling-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['scheduling-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['scheduling-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
      <ul :class="styles['scheduling-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['scheduling-menu-item'], activeMenu === item.label ? styles['scheduling-active-menu'] : '']"
          role="button"
          tabindex="0"
          @click="handleMenuClick(item.label)"
        >
          <i :class="[item.icon]" style="margin-right: 10px;"></i>
          {{ item.label }}
        </li>
      </ul>
    </aside>
    
    <!-- Conteúdo principal da página -->
    <main :class="styles['scheduling-main-content']">
      <div :class="styles['scheduling-header-row']">
        <div :class="styles['scheduling-top-bar']">
          <div :class="styles['scheduling-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['scheduling-user-underline-box']">
              <div :class="[styles['scheduling-user-underline'], styles.short]"></div>
              <div :class="[styles['scheduling-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/default-user.jpg')"
            alt="Foto do usuário" 
            :class="styles['scheduling-user-photo']" 
          />
        </div>     
      </div>

      <!-- Seção de Consultas -->
      <div :class="styles['scheduling-content']">
        <h2 :class="styles['scheduling-section-title']">Consultas</h2>
        
        <div :class="styles['scheduling-table-container']">
          <table :class="styles['scheduling-table']">
            <thead>
              <tr>
                <th>Profissional</th>
                <th>Especialização</th>
                <th>Data</th>
                <th>Hora</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(consulta, index) in consultas" :key="index">
                <td>{{ consulta.profissional }}</td>
                <td>{{ consulta.especializacao }}</td>
                <td>{{ consulta.data }}</td>
                <td>{{ consulta.hora }}</td>
                <td>
                  <span :class="[styles['scheduling-status'], styles[consulta.status.toLowerCase()]]">
                    {{ consulta.status }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/SchedulingView.module.css';

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
      activeMenu: 'CONSULTAS',
      consultas: [
        {
          profissional: 'Dr. João Pereira',
          especializacao: 'Cardiologista',
          data: '15/04',
          hora: '09:00',
          status: 'Agendado'
        },
        {
          profissional: 'Dra. Ana Oliveira',
          especializacao: 'Ortopedista',
          data: '15/04',
          hora: '10:30',
          status: 'Agendado'
        },
        {
          profissional: 'Dr. João Pereira',
          especializacao: 'Cardiologista',
          data: '10/03',
          hora: '15:30',
          status: 'Finalizado'
        },
        {
          profissional: 'Dr. João Pereira',
          especializacao: 'Cardiologista',
          data: '08/03',
          hora: '12:30',
          status: 'Cancelado'
        },
        {
          profissional: 'Dr. João Pereira',
          especializacao: 'Cardiologista',
          data: '08/03',
          hora: '12:30',
          status: 'Cancelado'
        }
        
        
      ]
    };
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
    }
  }
};
</script>