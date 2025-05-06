<template>
  <div :class="styles.container">
    
    <!-- ==== SIDEBAR - Menu Lateral ==== -->
    <aside :class="styles.sidebar">
      <!-- Logo -->
      <div :class="styles.logoBox">
        <img :src="require('../assets/logo.png')" alt="Logo Agenda Fácil" :class="styles.logo" />
      </div>

      <!-- Lista de Itens do Menu -->
      <ul :class="styles.menuList">
        <li 
          v-for="item in menuItems" 
          :key="item" 
          :class="[styles.menuItem, activeMenu === item ? styles.activeMenu : '']"
          @click="setActiveMenu(item)"
        >
          {{ item }}
        </li>
      </ul>
    </aside>

    <!-- ==== MAIN CONTENT ==== -->
    <main :class="styles.mainContent">
      
      <!-- Topo com informações do usuário e calendário -->
      <div :class="styles.headerRow">
        
        <!-- Informações do usuário -->
        <div :class="styles.topBar">
          <div :class="styles.userInfo">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles.userUnderlineBox">
              <div :class="[styles.userUnderline, styles.short]"></div>
              <div :class="[styles.userUnderline, styles.long]"></div>
            </div>
          </div>
          <img :src="userPhoto" alt="Foto do usuário" :class="styles.userPhoto" />
        </div>

        <!-- Calendário (em desenvolvimento) -->
        <div :class="styles.calendarBox">
          <h2>Calendário</h2>
          <p>[Calendário - Em desenvolvimento]</p>
        </div>
      </div>

      <!-- Corpo principal: mensagens e agenda -->
      <div :class="styles.contentBody">
        
        <!-- Seção de Mensagens -->
        <section :class="styles.chatSection">
          <h2>Mensagens</h2>
          <div :class="styles.messageCardsContainer">
            <div :class="styles.messageCard" v-for="(msg, i) in messages" :key="i">
              <div class="msg-header">
                <img :src="require('../assets/User.jpg')" alt="Avatar" class="msg-avatar" />
                <strong>{{ msg.doctor }}</strong>
              </div>
              <p>{{ msg.message }}</p>
            </div>
          </div>
        </section>

        <!-- Seção da Agenda -->
        <section :class="styles.agendaSection">
          <h2>Agenda</h2>
          <div :class="styles.agendaBox">
            <p>[Agenda - Em desenvolvimento]</p>
          </div>
        </section>

      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/HomeView.module.css';

export default {
  data() {
    return {
      styles,
      userName: 'Marcos',
      userPhoto: require('../assets/User.jpg'),
      menuItems: [
        'INÍCIO',
        'CONSULTAS',
        'PROFISSIONAIS',
        'PACIENTE',
        'MENSAGENS',
        'CONFIGURAÇÕES',
        'SAIR'
      ],
      activeMenu: 'INÍCIO',
      messages: [
        { doctor: 'Dr. João Pereira', message: 'Sua consulta está agendada para HOJE às 08:00' },
        { doctor: 'Dra. Ana Oliveira', message: 'Sua consulta está agendada para HOJE às 10:30' }
      ]
    };
  },
  methods: {
    setActiveMenu(item) {
      this.activeMenu = item;
    }
  }
};
</script>
