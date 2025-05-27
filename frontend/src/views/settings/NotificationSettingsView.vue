<template>
  <div :class="styles['notificationsettings-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['notificationsettings-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['notificationsettings-logo-box']">
        <img 
          :src="require('../../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['notificationsettings-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
      <ul :class="styles['notificationsettings-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['notificationsettings-menu-item'], activeMenu === item.label ? styles['notificationsettings-active-menu'] : '']"
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
    <main :class="styles['notificationsettings-main-content']">
      <!-- Topo com saudação e foto -->
      <div :class="styles['notificationsettings-header-row']">
        <div :class="styles['notificationsettings-top-bar']">
          <div :class="styles['notificationsettings-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['notificationsettings-user-underline-box']">
              <div :class="[styles['notificationsettings-user-underline'], styles.short]"></div>
              <div :class="[styles['notificationsettings-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['notificationsettings-user-photo']" 
          />
        </div>     
      </div>

      <!-- Conteúdo de notificações -->
      <section :class="styles['notificationsettings-content']">
        <h2 :class="styles['notificationsettings-title']">Notificações</h2>

        <div :class="styles['notificationsettings-option']">
          <span>Notificação por E-Mail</span>
          <label class="switch">
            <input type="checkbox" v-model="emailNotification">
            <span class="slider round"></span>
          </label>
        </div>

        <div :class="styles['notificationsettings-option']">
          <span>Notificação por SMS</span>
          <label class="switch">
            <input type="checkbox" v-model="smsNotification">
            <span class="slider round"></span>
          </label>
        </div>

        <div :class="styles['notificationsettings-option']">
          <span>Lembrete de Consultas (01 Dia Antes)</span>
          <label class="switch">
            <input type="checkbox" v-model="appointmentReminder">
            <span class="slider round"></span>
          </label>
        </div>

        <div :class="styles['notificationsettings-link']" @click="goToSounds">
          Sons e Alertas >
        </div>

        <div :class="styles['notificationsettings-link']" @click="goBack">
          Voltar >
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/NotificationSettingsView.module.css';

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
      emailNotification: true,
      smsNotification: true,
      appointmentReminder: true,
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
    },
    goToSounds() {
      this.$router.push('/settings/sounds');
    },
    goBack() {
      this.$router.back();
    }
  }
};
</script>
