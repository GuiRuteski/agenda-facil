<template>
  <div :class="styles['login-container']">
    <form :class="styles['login-form']" @submit.prevent="handleLogin">
      <img src="../assets/logo.png" alt="Logo" :class="styles['login-logo']" />

      <input v-model="email" type="email" placeholder="Email" :class="styles['login-input']" required />
      <input v-model="password" type="password" placeholder="Senha" :class="styles['login-input']" required />
      <p :class="styles['login-forgot-password']">Esqueci minha senha</p>
      <button type="submit" :class="styles['login-button']">Entrar</button>
      <p :class="styles['login-create-account']">
        Ainda não tem conta? <router-link to="/register">Clique para criar uma conta</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import styles from '@/assets/css/LoginView.module.css';

export default {
  data() {
    return {
      email: '',
      password: '',
      styles
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        });
        const token = response.data.access_token;
        localStorage.setItem('token', token);
        console.log('Login bem-sucedido. Token salvo.');
        this.$router.push('/home'); // ou outra rota que você queira redirecionar
      } catch (error) {
        console.error('Erro no login:', error);
        alert('Login inválido. Verifique o email e senha.');
      }
    }
  }
};
</script>