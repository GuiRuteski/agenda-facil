<template>
  <div :class="styles['login-container']">
    <form :class="styles['login-form']" @submit.prevent="handleLogin">
      <img src="../assets/logo.png" alt="Logo" :class="styles['login-logo']" />

      <input v-model="email" type="email" placeholder="Email" :class="styles['login-input']" required />
      <input v-model="password" type="password" placeholder="Senha" :class="styles['login-input']" required />
      <p :class="styles['login-forgot-password']">Esqueci minha senha</p>
      <button type="submit" :class="styles['login-button']">ENTRAR</button>
      <p :class="styles['login-create-account']">
        Ainda não tem conta? <router-link to="/register">Clique para criar uma conta</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import api from '../services/axios'
import styles from '@/assets/css/LoginView.module.css'

export default {
  data() {
    return {
      email: '',
      password: '',
      styles
    }
  },
  methods: {
    async handleLogin() {
  try {
    const response = await api.post('/auth/login', {
      email: this.email,
      senha: this.password
    })

    const token = response.data.access_token
    const tipoConta = response.data.tipoConta || response.data.tipo // ajuste conforme o backend

    localStorage.setItem('token', token)
    localStorage.setItem('tipoConta', tipoConta)

    if (tipoConta === 'Paciente') {
      this.$router.push('/home')
    } else if (tipoConta === 'RECEPCIONISTA') {
      this.$router.push('/homesecretary')
    } else {
      this.$router.push('/home') // padrão
    }
  } catch (error) {
    console.error('Erro no login:', error)
    alert(error.response?.data?.erro || 'Login inválido. Verifique o email e senha.')
  }
}
  }
}
</script>
