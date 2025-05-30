<template>
  <div :class="styles['scheduling-container']">
    <aside :class="styles['scheduling-sidebar']">
      <div :class="styles['scheduling-logo-box']">
        <img 
          :src="require('../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['scheduling-logo']" 
        />
      </div>
      <ul :class="styles['scheduling-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['scheduling-menu-item'], activeMenu === item.label ? styles['scheduling-active-menu'] : '']"
          role="button"
          tabindex="0"
          @click="handleMenuClick(item.label)"
        >
          <i :class="[item.icon]" style="margin-right: 10px;"></i>
          {{ item.label }}
        </li>
      </ul>
    </aside>

    <main :class="styles['scheduling-main-content']">
      <div :class="styles['scheduling-header-row']">
        <div :class="styles['scheduling-top-bar']">
          <div :class="styles['scheduling-user-info']">
            <h1>Olá, Dr. {{ userName }}!</h1>
            <div :class="styles['scheduling-user-underline-box']">
              <div :class="[styles['scheduling-user-underline'], styles.short]"></div>
              <div :class="[styles['scheduling-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../assets/default-user.jpg')"
            alt="Foto do usuário" 
            :class="styles['scheduling-user-photo']" 
          />
        </div>     
      </div>

      <div :class="styles['scheduling-content']">
        <h2 :class="styles['scheduling-section-title']">Solicitações de Consulta</h2>

        <div :class="styles['scheduling-table-container']">
          <table :class="styles['scheduling-table']">
            <thead>
              <tr>
                <th>Paciente</th>
                <th>Ficha</th>
                <th>Data</th>
                <th>Hora</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(consulta, index) in consultas" :key="index">
                <td>{{ consulta.paciente }}</td>
                <td><a href="#" @click.prevent="exibirFicha(consulta)"><em>Exibir</em></a></td>
                <td>{{ consulta.data }}</td>
                <td>{{ consulta.hora }}</td>
                <td>
                  <span :class="[styles['scheduling-status'], styles[consulta.status.toLowerCase()]]">
                    {{ consulta.status }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/SchedulingDoctorView.module.css'
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
      activeMenu: 'AGENDAMENTOS',
      consultas: [
        {
          paciente: 'Sr. Marcos',
          data: '15/04',
          hora: '09:00',
          status: 'Agendado'
        },
        {
          paciente: 'Sr. Marcos',
          data: '15/04',
          hora: '10:30',
          status: 'Agendado'
        },
        {
          paciente: 'Sr. Marcos',
          data: '10/03',
          hora: '15:30',
          status: 'Finalizado'
        },
        {
          paciente: 'Sr. Marcos',
          data: '08/03',
          hora: '12:30',
          status: 'Cancelado'
        }
      ]
    }
  },
  created() {
    this.getUserName()
  },
  methods: {
    async getUserName() {
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
          this.$router.push('/homedoctor')
          break
        case 'AGENDAMENTOS':
          this.$router.push('/schedulingdoctor')
          break
        case 'MENSAGENS':
          this.$router.push('/messagedoctor')
          break
        case 'CONFIGURAÇÕES':
          this.$router.push('/settingsdoctor')
          break
        case 'SAIR':
          this.logout()
          break
      }
    },
    logout() {
      this.$router.push('/login')
    },
    exibirFicha(consulta) {
      alert(`Exibindo ficha de ${consulta.paciente}`)
      // Aqui você pode abrir um modal ou navegar para outra tela com mais detalhes da ficha.
    }
  }
}
</script>
