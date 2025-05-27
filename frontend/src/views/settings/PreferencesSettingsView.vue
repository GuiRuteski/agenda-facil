<template>
  <div :class="styles['preferencessettings-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['preferencessettings-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['preferencessettings-logo-box']">
        <img 
          :src="require('../../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['preferencessettings-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
      <ul :class="styles['preferencessettings-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['preferencessettings-menu-item'], activeMenu === item.label ? styles['preferencessettings-active-menu'] : '']"
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
    <main :class="styles['preferencessettings-main-content']">
      <div :class="styles['preferencessettings-header-row']">
        <div :class="styles['preferencessettings-top-bar']">
          <div :class="styles['preferencessettings-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['preferencessettings-user-underline-box']">
              <div :class="[styles['preferencessettings-user-underline'], styles.short]"></div>
              <div :class="[styles['preferencessettings-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['preferencessettings-user-photo']" 
          />
        </div>     
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/PreferencesSettingsView.module.css';

export default {
  data() {
    return {
      styles,
      userName: 'Marcos',
      userPhoto: require('../../assets/User.jpg'),
      menuItems: [
        { label: 'INÍCIO', icon: 'fas fa-home' },
        { label: 'CONSULTAS', icon: 'fas fa-calendar-check' },
        { label: 'PROFISSIONAIS', icon: 'fas fa-user-md' },
        { label: 'PACIENTE', icon: 'fas fa-user' },
        { label: 'MENSAGENS', icon: 'fas fa-comments' },
        { label: 'CONFIGURAÇÕES', icon: 'fas fa-cog' },
        { label: 'SAIR', icon: 'fas fa-sign-out-alt' }
      ],
      activeMenu: 'CONFIGURAÇÕES',
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
