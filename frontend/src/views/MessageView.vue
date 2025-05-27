<template>
  <div :class="styles['message-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['message-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['message-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['message-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
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

    <!-- Conteúdo principal da página -->
    <main :class="styles['message-main-content']">
      <!-- Cabeçalho com saudação -->
      <div :class="styles['message-header-row']">
        <div :class="styles['message-top-bar']">
          <div :class="styles['message-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
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

      <!-- Caixa de Mensagens -->
      <section :class="styles['message-box']">
        <h2 :class="styles['message-box-title']">Caixa de Mensagens</h2>
        <ul :class="styles['message-list']">
          <li v-for="(message, index) in messages" :key="index" :class="styles['message-item']">
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
import styles from '@/assets/css/MessageView.module.css';

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
      activeMenu: 'MENSAGENS',
      messages: [
        {
          sender: 'Dr. João Pereira',
          subject: 'Consulta',
          text: 'Sua consulta está agendada para HOJE às 09:00',
          date: '15/04'
        },
        {
          sender: 'Dra. Ana Oliveira',
          subject: 'Consulta',
          text: 'Sua consulta está agendada para HOJE às 10:30',
          date: '15/04'
        },
        {
          sender: 'Dr. João Pereira',
          subject: 'Consulta',
          text: 'Bom dia, em qual horário podemos marcar o retorno?',
          date: '10/03'
        },
        {
          sender: 'Dr. João Pereira',
          subject: 'Cancelamento de Consulta',
          text: 'Boa tarde, desmarquei seu horário das 15:30, deseja remarcar?',
          date: '08/03'
        },
        {
          sender: 'Dr. Rubens Silva',
          subject: 'Dúvidas',
          text: 'Boa tarde, infelizmente estarei de férias durante essa semana.',
          date: '01/03'
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
