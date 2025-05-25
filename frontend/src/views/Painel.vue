<template>
  <div class="painel">
    <h1>Bem-vindo, {{ usuario.nome }}</h1>
    <p><strong>Email:</strong> {{ usuario.email }}</p>
    <p> v-if="usuario.funcionario"></p>
      <p><strong>Tipo:</strong> {{ usuario.funcionario.tipo }}</p>
      <p><strong>Nome:</strong> {{ usuario.funcionario.nome }}</p>
      <p><strong>CRM:</strong> {{ usuario.funcionario.crm || 'N/A' }}</p>
      <p><strong>Telefone:</strong> {{ usuario.funcionario.telefone || 'N/A' }}</p>
      <p><strong>Endereço:</strong> {{ usuario.funcionario.endereco || 'N/A' }}</p>
      <p><strong>Data de Nascimento:</strong> {{ usuario.funcionario.data_nascimento || 'N/A' }}</p>

      <strong>Especialidade:</strong> {{ usuario.funcionario.especialidade || 'N/A' }}
    
    <button @click="logout">Sair</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PainelView',
  data() {
    return {
      usuario: {}
    }
  },
  async created() {
    try {
      const res = await axios.get('http://localhost:5000/api/auth/me', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      this.usuario = res.data
    } catch (error) {
      console.error('Erro ao carregar usuário:', error)
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
