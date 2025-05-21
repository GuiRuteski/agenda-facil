<template>
  <div :class="styles['register-container']">
    <form @submit.prevent="handleRegister" :class="styles['register-form']">
      <img src="../assets/logo.png" alt="Logo" :class="styles['register-logo']" />
      
      <div :class="styles['register-form-row']">
        <input v-model="email" type="email" placeholder="E-Mail" :class="styles['register-input']" required />
        <input v-model="cpf" type="text" placeholder="CPF" :class="styles['register-input']" required />
      </div>

      <div :class="styles['register-form-row']">
        <input v-model="password" type="password" placeholder="Senha" :class="styles['register-input']" required />
        <select v-model="accountType" :class="styles['register-select']" required>
          <option value="" disabled selected>Tipo de Conta</option>
          <option value="Paciente">Paciente</option>
          <option value="Médico">Médico</option>
          <option value="Secretario">Secretário</option>
        </select>
      </div>

      <div :class="styles['register-form-row']">
        <input v-model="confirmPassword" type="password" placeholder="Confirmar Senha" :class="styles['register-input']" required />
        <select v-model="gender" :class="styles['register-select']" required>
          <option value="" disabled selected>Sexo</option>
          <option value="Masculino">Masculino</option>
          <option value="Feminino">Feminino</option>
          <option value="Outro">Outro</option>
        </select>
      </div>

      <button type="submit" :class="styles['register-button']">CADASTRAR</button>

      <p :class="styles['register-login-link']">
        Já tem conta? <router-link to="/login">Fazer login</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import styles from '@/assets/css/RegisterView.module.css';

export default {
  data() {
    return {
      email: '',
      cpf: '',
      password: '',
      confirmPassword: '',
      gender: '',
      accountType: '',
      styles
    };
  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        alert('As senhas não coincidem.');
        return;
      }
      const dados = {
        email: this.email,
        cpf: this.cpf,
        senha: this.password,
        sexo: this.gender,
        tipoConta: this.accountType
      };
      try {
        await axios.post('http://localhost:5000/register', dados);
        console.log('Registro feito com sucesso!');
        this.$router.push('/login');
      } catch (error) {
        console.error('Erro no registro:', error);
      }
    }
  }
};
</script>