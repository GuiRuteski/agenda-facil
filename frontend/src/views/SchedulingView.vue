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
