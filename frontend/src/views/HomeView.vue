<template>
  <!-- Container principal da página -->
  <div :class="styles['home-container']">
    
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['home-sidebar']">
      
      <!-- Caixa do logotipo -->
      <div :class="styles['home-logo-box']">
        <!-- Imagem do logotipo -->
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['home-logo']" 
        />
      </div>
      
      <!-- Lista de menus laterais -->
      <ul :class="styles['home-menu-list']">
        <!-- Cada item do menu -->
        <li 
          v-for="item in menuItems" 
          :key="item" 
          :class="[styles['home-menu-item'], activeMenu === item ? styles['home-active-menu'] : '']"
          @click="setActiveMenu(item)"> <!-- Define o item como ativo ao clicar -->
          {{ item }}
        </li>
      </ul>
    </aside>

    <!-- Conteúdo principal da página -->
    <main :class="styles['home-main-content']">
      
      <!-- Linha superior com saudação e calendário -->
      <div :class="styles['home-header-row']">
        
        <!-- Barra superior com dados do usuário -->
        <div :class="styles['home-top-bar']">
          
          <!-- Informações do usuário -->
          <div :class="styles['home-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            
            <!-- Linhas decorativas abaixo do nome -->
            <div :class="styles['home-user-underline-box']">
              <div :class="[styles['home-user-underline'], styles.short]"></div>
              <div :class="[styles['home-user-underline'], styles.long]"></div>
            </div>
          </div>

          <!-- Foto do usuário -->
          <img 
            :src="userPhoto" 
            alt="Foto do usuário" 
            :class="styles['home-user-photo']" 
          />
        </div>

        <!-- Caixa do calendário (em desenvolvimento) -->
        <div :class="styles['home-calendar-box']">
          <h2>Calendário</h2>
          <p>[Calendário - Em desenvolvimento]</p>
        </div>
      </div>

      <!-- Corpo principal com mensagens e agenda -->
      <div :class="styles['home-content-body']">

        <!-- Seção de mensagens -->
        <section :class="styles['home-chat-section']">
          <h2>Mensagens:</h2>

          <!-- Container dos cards de mensagens -->
          <div :class="styles['home-message-cards-container']">
            
            <!-- Cada card representa um profissional com mensagens -->
            <div 
              v-for="(doctor, i) in messages" 
              :key="i" 
              :class="styles['home-message-card']"
            >
              <!-- Cabeçalho do card com avatar e nome -->
              <div :class="styles['home-msg-header']">
                <img :src="doctor.avatar" alt="Avatar" :class="styles['home-msg-avatar']" />
                <strong>{{ doctor.name }}</strong>
              </div>

              <!-- Lista de mensagens do profissional -->
              <div 
                v-for="(msg, j) in doctor.messages" 
                :key="j" 
                :class="styles['home-message-bubble']"
              >
                <p>{{ msg.text }}</p>
                <span :class="styles['home-message-date']">{{ msg.date }}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Seção da agenda (também em desenvolvimento) -->
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
// Importa os estilos em CSS Modules
import styles from '@/assets/css/HomeView.module.css';

export default {
  data() {
    return {
      styles,
      userName: 'Marcos', // Nome do usuário a ser exibido
      userPhoto: require('../assets/User.jpg'), // Caminho da foto do usuário
      menuItems: [ // Itens do menu lateral
        'INÍCIO',
        'CONSULTAS',
        'PROFISSIONAIS',
        'PACIENTE',
        'MENSAGENS',
        'CONFIGURAÇÕES',
        'SAIR'
      ],
      activeMenu: 'INÍCIO', // Item de menu atualmente ativo
      messages: [ // Lista de mensagens por profissional
        {
          name: 'Dr. João Pereira',
          avatar: require('../assets/User.jpg'),
          messages: [
            {
              text: 'Sua consulta está agendada para dia 15 de Abril às 09:00',
              date: '10/04'
            },
            {
              text: 'Sua consulta está agendada para HOJE às 09:00',
              date: '15/04'
            }
          ]
        },
        {
          name: 'Dra. Ana Oliveira',
          avatar: require('../assets/User.jpg'),
          messages: [
            {
              text: 'Sua consulta está agendada para dia 15 de Abril às 10:30',
              date: '05/04'
            },
            {
              text: 'Sua consulta está agendada para HOJE às 10:30',
              date: '15/04'
            }
          ]
        }
      ]
    };
  },
  methods: {
    // Define qual item do menu está ativo
    setActiveMenu(item) {
      this.activeMenu = item;
    }
  }
};
</script>
