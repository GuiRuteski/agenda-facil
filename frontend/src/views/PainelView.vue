<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="painel">
    <h1>Bem-vindo, {{ usuario.nome || 'Usuário' }}</h1>
    <p><strong>Email:</strong> {{ usuario.email }}</p>

    <div v-if="usuario.tipo === 'medico'">
      <p><strong>Especialidade:</strong> {{ usuario.especialidade || 'N/A' }}</p>
    </div>

    <div v-else-if="usuario.tipo === 'funcionario'">
      <p><strong>Tipo:</strong> {{ usuario.tipo_funcionario || 'N/A' }}</p>
    </div>

    <button @click="logout">Sair</button>
  </div>
</template>

<script>
import api from '../services/axios'

export default {
  name: 'PainelView',
  data() {
    return {
      usuario: {}
    }
  },
  async created() {
    try {
      const response = await api.get('/auth/me')
      this.usuario = response.data
    } catch (error) {
      console.error('Erro ao carregar o perfil:', error)
      alert('Sessão expirada ou inválida. Faça login novamente.')
      this.$router.push('/login')
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.painel {
  padding: 2rem;
  font-family: Arial, sans-serif;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>
