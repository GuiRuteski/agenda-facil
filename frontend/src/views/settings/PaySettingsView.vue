<template>
  <div :class="styles['paysettings-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['paysettings-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['paysettings-logo-box']">
        <img 
          :src="require('../../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['paysettings-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
      <ul :class="styles['paysettings-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['paysettings-menu-item'], activeMenu === item.label ? styles['paysettings-active-menu'] : '']"
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
    <main :class="styles['paysettings-main-content']">
      <div :class="styles['paysettings-header-row']">
        <div :class="styles['paysettings-top-bar']">
          <div :class="styles['paysettings-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['paysettings-user-underline-box']">
              <div :class="[styles['paysettings-user-underline'], styles.short]"></div>
              <div :class="[styles['paysettings-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['paysettings-user-photo']" 
          />
        </div>     
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/PaySettingsView.module.css';

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
