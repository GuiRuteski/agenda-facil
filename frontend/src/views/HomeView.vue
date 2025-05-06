<template>
  <div :class="styles.container">
    
    <!-- ===== SIDEBAR (Menu Lateral) ===== -->
    <aside :class="styles.sidebar">
      <div :class="styles.logoBox">
        <img :src="require('../assets/logo.png')" alt="Logo Agenda Fácil" :class="styles.logo" />
      </div>
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

    <!-- ===== MAIN CONTENT ===== -->
    <main :class="styles.mainContent">
      
      <!-- TOPO: Barra do Usuário + Calendário -->
      <div :class="styles.headerRow">
        <div :class="styles.topBar">
          <h1>Olá, Sr. {{ userName }}!</h1>
          <img :src="userPhoto" alt="Foto do usuário" :class="styles.userPhoto" />
        </div>
        <div :class="styles.calendarBox">
          <h2>Calendário</h2>
          <p>[Calendário - Em desenvolvimento]</p>
        </div>
      </div>

      <!-- Sublinhos decorativos -->
      <div :class="styles.userUnderlineBox">
        <div :class="[styles.userUnderline, styles.short]"></div>
        <div :class="[styles.userUnderline, styles.long]"></div>
      </div>

      <!-- Corpo: Mensagens e Agenda lado a lado -->
      <div :class="styles.contentBody">
        
        <!-- MENSAGENS -->
        <section :class="styles.chatSection">
          <h2>Mensagens</h2>
          <div :class="styles.messageCardsContainer">
            <div :class="styles.messageCard">
              <div class="msg-header">
                <img :src="require('../assets/User.jpg')" alt="Dr. João Pereira" class="msg-avatar" />
                <strong>Dr. João Pereira</strong>
              </div>
              <p>Sua consulta está agendada para HOJE às 08:00</p>
            </div>
            <div :class="styles.messageCard">
              <div class="msg-header">
                <img :src="require('../assets/User.jpg')" alt="Dra. Ana Oliveira" class="msg-avatar" />
                <strong>Dra. Ana Oliveira</strong>
              </div>
              <p>Sua consulta está agendada para HOJE às 10:30</p>
            </div>
          </div>
        </section>

        <!-- AGENDA -->
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
      activeMenu: 'INÍCIO'
    };
  },
  methods: {
    setActiveMenu(item) {
      this.activeMenu = item;
    }
  }
};
</script>
