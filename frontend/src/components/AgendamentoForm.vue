<template>
  <div>
    <h2>Agendar Consulta</h2>
    <form @submit.prevent="criarAgendamento">
      <label>Paciente:</label>
      <select v-model="paciente_id" required>
        <option disabled value="">Selecione um paciente</option>
        <option v-for="p in pacientes" :key="p.id" :value="p.id">
          {{ p.nome }}
        </option>
      </select>

      <label>Profissional:</label>
      <select v-model="profissional_id" required>
        <option disabled value="">Selecione um profissional</option>
        <option v-for="f in profissionais" :key="f.id" :value="f.id">
          {{ f.nome }}
        </option>
      </select>

      <label>Data e hora:</label>
      <input v-model="data_hora" type="datetime-local" required />

      <label>Status:</label>
      <select v-model="status" required>
        <option value="Agendado">Agendado</option>
        <option value="Cancelado">Cancelado</option>
        <option value="Concluído">Concluído</option>
      </select>

      <button type="submit">Agendar</button>
    </form>
    <p v-if="mensagem">{{ mensagem }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      paciente_id: '',
      profissional_id: '',
      data_hora: '',
      status: 'Agendado',
      mensagem: '',
      pacientes: [],
      profissionais: []
    };
  },
  mounted() {
    this.carregarPacientes();
    this.carregarProfissionais();
  },
  methods: {
    async carregarPacientes() {
      try {
        const res = await axios.get('http://localhost:5000/api/pacientes');
        this.pacientes = res.data;
      } catch (err) {
        console.error('Erro ao carregar pacientes:', err);
      }
    },
    async carregarProfissionais() {
      try {
        const res = await axios.get('http://localhost:5000/api/funcionarios');
        this.profissionais = res.data;
      } catch (err) {
        console.error('Erro ao carregar profissionais:', err);
      }
    },
    async criarAgendamento() {
      try {
        await axios.post('http://localhost:5000/api/agendamentos', {
          paciente_id: this.paciente_id,
          profissional_id: this.profissional_id,
          data_hora: this.data_hora,
          status: this.status
        });
        this.mensagem = 'Agendamento criado com sucesso!';
        this.paciente_id = '';
        this.profissional_id = '';
        this.data_hora = '';
        this.status = 'Agendado';
      } catch (error) {
        this.mensagem = 'Erro ao criar agendamento.';
        console.error(error);
      }
    }
  }
};
</script>
