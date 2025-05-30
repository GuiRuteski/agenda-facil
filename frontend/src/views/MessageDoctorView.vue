<template>
  <div :class="styles['message-container']">
    <!-- Sidebar -->
    <aside :class="styles['message-sidebar']">
      <div :class="styles['message-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['message-logo']" 
        />
      </div>
      <ul :class="styles['message-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['message-menu-item'], activeMenu === item.label ? styles['message-active-menu'] : '']"
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
    <main :class="styles['message-main-content']">
      <div :class="styles['message-header-row']">
        <div :class="styles['message-top-bar']">
          <div :class="styles['message-user-info']">
            <h1>Olá, Dr. {{ userName || 'Médico(a)' }}!</h1>
            <div :class="styles['message-user-underline-box']">
              <div :class="[styles['message-user-underline'], styles.short]"></div>
              <div :class="[styles['message-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['message-user-photo']" 
          />
        </div>     
      </div>

      <!-- Caixa de mensagens -->
      <section :class="styles['message-box']">
        <h2 :class="styles['message-box-title']">Caixa de Mensagens</h2>
        <ul :class="styles['message-list']">
          <li 
            v-for="(message, index) in messages" 
            :key="index" 
            :class="styles['message-item']"
          >
            <div :class="styles['message-avatar']">
              <img :src="require('../assets/User.jpg')" alt="Avatar" />
            </div>
            <div :class="styles['message-content']">
              <strong>{{ message.sender }} - {{ message.subject }}</strong>
              <p>{{ message.text }}</p>
            </div>
            <div :class="styles['message-date']">
              {{ message.date }}
            </div>
          </li>
        </ul>
      </section>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/MessageView.module.css'
import api from '@/services/axios'

export default {
  data() {
    return {
      styles,
      userName: '',
      userPhoto: require('../assets/User.jpg'),
      menuItems: [
        { label: 'INÍCIO', icon: 'fas fa-home' },
        { label: 'AGENDAMENTOS', icon: 'fas fa-calendar-check' },
        { label: 'MENSAGENS', icon: 'fas fa-comments' },
        { label: 'CONFIGURAÇÕES', icon: 'fas fa-cog' },
        { label: 'SAIR', icon: 'fas fa-sign-out-alt' }
      ],
      activeMenu: 'MENSAGENS',
      messages: [
        {
          sender: 'Sra. Renata',
          subject: 'Consulta',
          text: 'Dr. confirmei a consulta do Sr. Marcos para hoje ok?',
          date: '15/04'
        },
        {
          sender: 'Sra. Renata',
          subject: 'Consulta',
          text: 'Dra. acabei de confirmar a consulta do Sr. Marcos',
          date: '15/04'
        },
        {
          sender: 'Sra. Renata',
          subject: 'Consulta',
          text: 'Bom dia, infelizmente foi desmarcado, vou ver com ele um novo horário.',
          date: '10/03'
        },
        {
          sender: 'Sra. Renata',
          subject: 'Cancelamento de Consulta',
          text: 'Boa tarde, desmarquei seu horário das 15:30, deseja remarcar?',
          date: '08/03'
        },
        {
          sender: 'Sra. Renata',
          subject: 'Dúvidas',
          text: 'Boa tarde, infelizmente o dr. está de férias durante esta semana.',
          date: '01/03'
        }
      ]
    };
  },
  async created() {
    try {
      const response = await api.get('/auth/me')
      this.userName = response.data.nome
    } catch (error) {
      console.error('Erro ao carregar nome do usuário:', error)
      this.$router.push('/login')
    }
  },
  methods: {
    handleMenuClick(label) {
      this.activeMenu = label;
      const routes = {
        'INÍCIO': '/homedoctor',
        'AGENDAMENTOS': '/schedulingdoctor',
        'MENSAGENS': '/messagedoctor',
        'CONFIGURAÇÕES': '/settingsdoctor',
      };

      if (label === 'SAIR') {
        localStorage.removeItem('token');
        this.$router.push('/login');
      } else if (routes[label]) {
        this.$router.push(routes[label]);
      }
    }
  }
}
</script>
