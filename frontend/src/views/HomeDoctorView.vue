<template>
  <div :class="styles['home-container']">
    <!-- Sidebar -->
    <aside :class="styles['home-sidebar']">
      <div :class="styles['home-logo-box']">
        <img :src="require('../assets/logo.png')" alt="Logo Agenda Fácil" :class="styles['home-logo']" />
      </div>

      <ul :class="styles['home-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['home-menu-item'], activeMenu === item.label ? styles['home-active-menu'] : '']"
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
    <main :class="styles['home-main-content']">
      <div :class="styles['home-header-row']">
        <div :class="styles['home-top-bar']">
          <div :class="styles['home-user-info']">
            <h1>Olá, {{ user.nome || 'Médico(a)' }}!</h1>
            <div :class="styles['home-user-underline-box']">
              <div :class="[styles['home-user-underline'], styles.short]"></div>
              <div :class="[styles['home-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/default-user.jpg')"
            alt="Foto do usuário" 
            :class="styles['home-user-photo']" 
          />
        </div>

        <div :class="styles['home-calendar-box']">
          <h2>Abril 2025</h2>
          <p>[Calendário - Em desenvolvimento]</p>
        </div>
      </div>

      <div :class="styles['home-content-body']">
        <section :class="styles['home-chat-section']">
          <h2>Mensagens:</h2>
          <div :class="styles['home-message-cards-container']">
            <div 
              v-for="(patient, i) in messages" 
              :key="i" 
              :class="styles['home-message-card']"
            >
              <div :class="styles['home-msg-header']">
                <img :src="patient.avatar" alt="Avatar" :class="styles['home-msg-avatar']" />
                <strong>{{ patient.name }}</strong>
              </div>
              <div 
                v-for="(msg, j) in patient.messages" 
                :key="j" 
                :class="styles['home-message-bubble']"
              >
                <p>{{ msg.text }}</p>
                <span :class="styles['home-message-date']">{{ msg.date }}</span>
              </div>
            </div>
          </div>
        </section>

        <section :class="styles['home-agenda-section']">
          <h2>Agenda</h2>
          <div>
            <p>[Agenda - Em desenvolvimento]</p>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script>
import api from '@/services/axios'
import styles from '@/assets/css/HomeView.module.css'

export default {
  data() {
    return {
      styles,
      user: {},
      userPhoto: require('../assets/User.jpg'),
      menuItems: [
        { label: 'INÍCIO', icon: 'fas fa-home' },
        { label: 'AGENDAMENTOS', icon: 'fas fa-calendar-check' },
        { label: 'MENSAGENS', icon: 'fas fa-comments' },
        { label: 'CONFIGURAÇÕES', icon: 'fas fa-cog' },
        { label: 'SAIR', icon: 'fas fa-sign-out-alt' }
      ],
      activeMenu: 'INÍCIO',
      messages: [] // Emulação visual
    }
  },
  async created() {
    try {
      const res = await api.get('/auth/me')
      this.user = res.data
    } catch (err) {
      console.error('Erro ao carregar usuário:', err)
      alert('Sessão expirada ou inválida. Faça login novamente.')
      this.$router.push('/login')
    }
  },
  methods: {
    handleMenuClick(label) {
      this.activeMenu = label
      const routeMap = {
        'INÍCIO': '/homedoctor',
        'AGENDAMENTOS': '/schedulingdoctor',
        'MENSAGENS': '/messagedoctor',
        'CONFIGURAÇÕES': '/settingsdoctor',
      }
      if (label === 'SAIR') {
        localStorage.removeItem('token')
        this.$router.push('/login')
      } else if (routeMap[label]) {
        this.$router.push(routeMap[label])
      }
    }
  }
}
</script>