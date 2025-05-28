<template>
  <div :class="styles['patient-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['patient-sidebar']">
      <!-- Caixa do logotipo -->
      <div :class="styles['patient-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['patient-logo']" 
        />
      </div>

      <!-- Lista de menus laterais -->
      <ul :class="styles['patient-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['patient-menu-item'], activeMenu === item.label ? styles['patient-active-menu'] : '']"
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
    <main :class="styles['patient-main-content']">
      <div :class="styles['patient-header-row']">
        <div :class="styles['patient-top-bar']">
          <div :class="styles['patient-user-info']">
<<<<<<< HEAD
            <h1>Olá, Sr. {{ userName }}!</h1>
=======
            <h1>Olá, {{ userName }}!</h1>
>>>>>>> 8b5e3b5f (Remover node_modules do repositório)
            <div :class="styles['patient-user-underline-box']">
              <div :class="[styles['patient-user-underline'], styles.short]"></div>
              <div :class="[styles['patient-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['patient-user-photo']" 
          />
        </div>     
      </div>

      <!-- Seção de informações do paciente -->
      <div :class="styles['patient-info-container']">
        <h2 :class="styles['patient-info-title']">Informações do Paciente</h2>
        
        <div :class="styles['patient-info-grid']">
          <!-- Nome -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Nome</label>
            <input 
              type="text" 
              v-model="patientData.name"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
          </div>
          
          <!-- Sexo -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Sexo</label>
            <select 
              v-model="patientData.gender"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
              <option value="">Selecione</option>
              <option value="Masculino">Masculino</option>
              <option value="Feminino">Feminino</option>
              <option value="Outro">Outro</option>
              <option value="Prefiro não informar">Prefiro não informar</option>
            </select>
          </div>
          
          <!-- Data de Nascimento -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Data de Nascimento</label>
            <input 
              type="date" 
              v-model="patientData.birthDate"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
          </div>
          
          <!-- Endereço -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Endereço</label>
            <input 
              type="text" 
              v-model="patientData.address"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
          </div>
          
          <!-- Número -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Número</label>
            <input 
              type="text" 
              v-model="patientData.addressNumber"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
          </div>
          
          <!-- CEP -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">CEP</label>
            <input 
              type="text" 
              v-model="patientData.cep"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"
            >
          </div>
          
          <!-- Telefone -->
          <div :class="styles['patient-info-group']">
            <label :class="styles['patient-info-label']">Telefone</label>
            <input 
              type="tel" 
              v-model="patientData.phone"
              :class="styles['patient-info-input']"
              :disabled="!isEditing"

            >
          </div>
        </div>

        <!-- Botões de ação -->
          <div :class="styles['patient-actions']">
            <button 
            :class="[styles['patient-action-button'], styles['primary']]"
            @click="toggleEdit"
          >
            {{ isEditing ? 'Salvar' : 'Editar' }}
            </button>
  
          <button 
            v-if="isEditing"
            :class="[styles['patient-action-button'], styles['secondary']]"
            @click="cancelEdit"
         >
          Cancelar
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/PatientView.module.css'
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
      activeMenu: 'PACIENTE',
      isEditing: false,
      patientData: {
        name: '',
        gender: '',
        birthDate: '',
        address: '',
        addressNumber: '',
        cep: '',
        phone: ''
      },
      originalData: {} // Para guardar os dados originais durante a edição
    };
    }
  },
  created() {
    this.carregarNomeUsuario()

    // Simulação da busca dos dados do paciente
    setTimeout(() => {
      this.patientData = {
        name: 'Marcos Oliveira Souza',
        gender: 'Masculino',
        birthDate: '1991-10-05',
        address: 'R. 9 de Julho',
        addressNumber: '125',
        cep: '00000-000',
        phone: '(12) 3456-7890'
      }
    }, 500)
  },
  methods: {
    async carregarNomeUsuario() {
      try {
        const response = await api.get('/auth/me')
        this.userName = response.data.nome
      } catch (error) {
        console.error('Erro ao carregar o nome do usuário:', error)
      }
    },
    
    logout() {
      this.$router.push('/login');
    },
    
    toggleEdit() {
      if (this.isEditing) {
        // Lógica para salvar os dados
        this.savePatientData();
      } else {
        // Entra no modo de edição
        this.originalData = JSON.parse(JSON.stringify(this.patientData));
        this.isEditing = true;
      }
    },
    
    cancelEdit() {
      // Restaura os dados originais
      this.patientData = JSON.parse(JSON.stringify(this.originalData));
      this.isEditing = false;
    },
    
    savePatientData() {
      // Aqui você implementaria a chamada à API para salvar os dados
      console.log('Dados do paciente salvos:', this.patientData);
      
      // Simulação de sucesso
      this.isEditing = false;
      alert('Informações atualizadas com sucesso!');
      
      // Em uma aplicação real, você faria:
      // api.savePatientData(this.patientData)
      //   .then(() => {
      //     this.isEditing = false;
      //     alert('Informações atualizadas com sucesso!');
      //   })
      //   .catch(error => {
      //     console.error('Erro ao salvar:', error);
      //     alert('Erro ao salvar informações');
      //   });

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

    logout() {
      this.$router.push('/login')
    },

    toggleEdit() {
      if (this.isEditing) {
        this.savePatientData()
      } else {
        this.originalData = JSON.parse(JSON.stringify(this.patientData))
        this.isEditing = true
      }
    },

    cancelEdit() {
      this.patientData = JSON.parse(JSON.stringify(this.originalData))
      this.isEditing = false
    },

    savePatientData() {
      console.log('Dados do paciente salvos:', this.patientData)
      this.isEditing = false
      alert('Informações atualizadas com sucesso!')
    }
  },
  
</script>
