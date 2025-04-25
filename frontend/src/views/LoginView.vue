<template>
  <div class="login">
    <form @submit.prevent="handleLogin">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Entrar</button>
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

<style scoped>
.login {
  max-width: 400px;
  margin: auto;
  padding: 1rem;
}
input {
  display: block;
  margin-bottom: 1rem;
  width: 100%;
  padding: 0.5rem;
}
button {
  width: 100%;
  padding: 0.5rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #45a049;
}
</style>