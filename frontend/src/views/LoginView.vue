<template>
  <div class="login">
    <form @submit.prevent="handleLogin">
      <img src="../assets/logo.png" alt="Logo" class="logo" />

      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <p class="forgot-password">Esqueci minha senha</p>
      <button type="submit">Entrar</button>
      <p class="create-account">
         Ainda não tem conta? <router-link to="/register">Clique para criar uma conta</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
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

<style src="@/assets/css/LoginView.css"></style>
