<template>
  <form @submit.prevent="criar">
    <input v-model="paciente_id" placeholder="ID do paciente" required />
    <input v-model="medico_id" placeholder="ID do médico" required />
    <input v-model="data_hora" placeholder="Data e Hora (YYYY-MM-DDTHH:mm)" required />
    <button type="submit">Agendar</button>
  </form>
</template>

<script>
import api from '../services/axios'

export default {
  data() {
    return {
      paciente_id: '',
      medico_id: '',
      data_hora: ''
    }
  },
  methods: {
    async criar() {
      try {
        const token = localStorage.getItem('token')
        await api.post('/api/agendamentos', {
          paciente_id: this.paciente_id,
          medico_id: this.medico_id,
          data_hora: this.data_hora
        }, {
          headers: { Authorization: `Bearer ${token}` }
        })
        alert('Agendamento criado!')
        this.$router.push('/home')
      } catch (err) {
        alert('Erro ao agendar.')
        console.error(err)
      }
    }
  }
}
</script>
