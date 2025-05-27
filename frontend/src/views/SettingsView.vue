<template>
  <div :class="styles['settings-container']">
    <!-- Barra lateral -->
    <aside :class="styles['settings-sidebar']">
      <div :class="styles['settings-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['settings-logo']" 
        />
      </div>
      <ul :class="styles['settings-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['settings-menu-item'], activeMenu === item.label ? styles['settings-active-menu'] : '']"
          role="button"
          tabindex="0"
          @click="handleMenuClick(item.label)"
        >
          <i :class="[item.icon]" style="margin-right: 10px;"></i>
          {{ item.label }}
        </li>
      </ul>
    </aside>

    <!-- Conteúdo principal -->
    <!-- Conteúdo principal da página -->
    <main :class="styles['settings-main-content']">
      <div :class="styles['settings-header-row']">
        <div :class="styles['settings-top-bar']">
          <div :class="styles['settings-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <h1>Olá, {{ userName }}!</h1>
            <div :class="styles['settings-user-underline-box']">
              <div :class="[styles['settings-user-underline'], styles.short]"></div>
              <div :class="[styles['settings-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['settings-user-photo']" 
          />
        </div>     
      </div>

      <!-- Seção de opções de configurações -->
      <section :class="styles['settings-options-section']">
        <h2 :class="styles['settings-options-title']">Configurações</h2>
        <div :class="styles['settings-options-box']">
          <div 
            v-for="option in settingsOptions" 
            :key="option.label" 
            :class="styles['settings-option-item']"
            @click="navigateToOption(option.route)"
            role="button"
            tabindex="0"
          >
            <span>{{ option.label }}</span>
            <i class="fas fa-chevron-right"></i>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/SettingsView.module.css'
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
      activeMenu: 'CONFIGURAÇÕES',
      settingsOptions: [
        { label: 'Dados da Conta', route: '/settings/account'},
        { label: 'Notificações', route: '/settings/notification'},
        { label: 'Preferencias', route: '/settings/preferences'},
        { label: 'Pagamentos', route: '/settings/payment'},
        { label: 'Suporte', route: '/settings/support'},
      ]
    };
      activeMenu: 'CONFIGURAÇÕES'
    }
  },
  created() {
    this.carregarNomeUsuario()
  },
  methods: {
    async carregarNomeUsuario() {
      try {
        const response = await api.get('/auth/me')
        this.userName = response.data.nome
      } catch (error) {
        console.error('Erro ao buscar nome do usuário:', error)
      }
    },
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
    navigateToOption(route) {
      this.$router.push(route);
    },
    logout() {
      this.$router.push('/login')
    }
  }

</script>

