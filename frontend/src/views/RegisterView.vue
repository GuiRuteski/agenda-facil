<template>
  <div class="register">
    <form @submit.prevent="handleRegister">
      <input v-model="name" type="text" placeholder="Nome" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Registrar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'; // <-- Adicione esta linha!

export default {
  data() {
    return {
      name: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async handleRegister() {
      const dados = {
        name: this.name,
        email: this.email,
        password: this.password
      };
      try {
        await axios.post('http://localhost:5000/register', dados);
        console.log('Registro feito com sucesso!');
        // redireciona ou mostra mensagem de sucesso
      } catch (error) {
        console.error('Erro no registro:', error);
      }
    }
  }
}
</script>

<style scoped>
.register {
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
  background-color: #2196F3;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #1976D2;
}
</style>