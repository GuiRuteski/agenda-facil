<template>
  <div :class="styles['register-container']">
    <form @submit.prevent="handleRegister" :class="styles['register-form']">
      <img src="../assets/logo.png" alt="Logo" :class="styles['register-logo']" />

      <!-- Campo Nome -->
      <div :class="styles['register-form-row']">
        <input v-model="nome" type="text" placeholder="Nome Completo" :class="styles['register-input']" required />
      </div>

      <!-- Email e CPF -->
      <div :class="styles['register-form-row']">
        <input v-model="email" type="email" placeholder="E-Mail" :class="styles['register-input']" required />
        <input
          v-model="cpf"
          @input="formatarCPF"
          type="text"
          placeholder="CPF"
          :class="styles['register-input']"
          maxlength="14"
          autocomplete="off"
          required
        />
      </div>

      <!-- Senha e Tipo -->
      <div :class="styles['register-form-row']">
        <input v-model="password" type="password" placeholder="Senha" :class="styles['register-input']" required />
        <select v-model="accountType" :class="styles['register-select']" required>
          <option value="" disabled selected>Tipo de Conta</option>
          <option value="Paciente">Paciente</option>
          <option value="Médico">Médico</option>
          <option value="Secretario">Secretário</option>
        </select>
      </div>

      <!-- Confirmar senha e sexo -->
      <div :class="styles['register-form-row']">
        <input v-model="confirmPassword" type="password" placeholder="Confirmar Senha" :class="styles['register-input']" required />
        <select v-model="gender" :class="styles['register-select']" required>
          <option value="" disabled selected>Sexo</option>
          <option value="Masculino">Masculino</option>
          <option value="Feminino">Feminino</option>
          <option value="Outro">Outro</option>
        </select>
      </div>

      <!-- Especialidade opcional -->
      <div v-if="accountType === 'Médico'" :class="styles['register-form-row']">
        <input v-model="especialidade" type="text" placeholder="Especialidade" :class="styles['register-input']" required />
      </div>

      <button type="submit" :class="styles['register-button']">CADASTRAR</button>

      <p :class="styles['register-login-link']">
        Já tem conta? <router-link to="/login">Fazer login</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import api from '../services/axios'
import styles from '@/assets/css/RegisterView.module.css'

export default {
  data() {
    return {
      nome: '',
      email: '',
      cpf: '',
      password: '',
      confirmPassword: '',
      gender: '',
      accountType: '',
      especialidade: '',
      styles
    }
  },
  methods: {
    formatarCPF() {
      // Remove tudo que não for número
      let digits = this.cpf.replace(/\D/g, '')
      // Limita a 11 números
      digits = digits.substring(0, 11)
      // Aplica a máscara
      if (digits.length <= 3) {
        this.cpf = digits
      } else if (digits.length <= 6) {
        this.cpf = `${digits.slice(0, 3)}.${digits.slice(3)}`
      } else if (digits.length <= 9) {
        this.cpf = `${digits.slice(0, 3)}.${digits.slice(3, 6)}.${digits.slice(6)}`
      } else {
        this.cpf = `${digits.slice(0, 3)}.${digits.slice(3, 6)}.${digits.slice(6, 9)}-${digits.slice(9)}`
      }
    },
    async handleRegister() {
      console.log('Tipo de conta selecionado:', this.accountType)
      if (this.password !== this.confirmPassword) {
        alert('As senhas não coincidem.')
        return
      }

      const cpfLimpo = this.cpf.replace(/\D/g, '')
        if (cpfLimpo.length !== 11) {
        alert('CPF inválido. Digite os 11 dígitos.')
        return
      }

      const dadosBase = {
        nome: this.nome,
        email: this.email,
        cpf: cpfLimpo,
        senha: this.password,
        sexo: this.gender
}

      let endpoint = ''
      let dados = {}

      if (this.accountType === 'Paciente') {
        endpoint = '/pacientes'
        dados = dadosBase
      } else if (this.accountType === 'Médico') {
        endpoint = '/medicos'
        dados = {
          ...dadosBase,
          especialidade: this.especialidade
        }
      } else if (this.accountType === 'Secretario') {
        endpoint = '/funcionarios'
        dados = {
          ...dadosBase,
          tipo: 'recepcionista'
        }
      } else {
        alert('Selecione um tipo de conta válido.')
        return
      }

      try {
        await api.post(endpoint, dados)
        alert('Cadastro realizado com sucesso!')
        this.$router.push('/login')
      } catch (error) {
        console.error('Erro no registro:', error)
        alert(error.response?.data?.erro || 'Erro ao registrar. Verifique os dados e tente novamente.')
      }
    }
  }
}
</script>
