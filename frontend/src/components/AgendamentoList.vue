<template>
  <div>
    <h2>Lista de Agendamentos</h2>

    <ul v-if="agendamentos.length > 0">
      <li v-for="a in agendamentos" :key="a.id">
        <strong>Paciente:</strong> {{ getPacienteNome(a.paciente_id) }} —
        <strong>Profissional:</strong> {{ getProfissionalNome(a.profissional_id) }} —
        <strong>Data:</strong> {{ formatarDataHora(a.data_hora) }} —
        <strong>Status:</strong> {{ a.status }}
      </li>
    </ul>

    <p v-else>Nenhum agendamento encontrado.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      agendamentos: [],
      pacientes: [],
      profissionais: []
    };
  },
  async mounted() {
    await Promise.all([
      this.carregarAgendamentos(),
      this.carregarPacientes(),
      this.carregarProfissionais()
    ]);
  },
  methods: {
    async carregarAgendamentos() {
      try {
        const response = await axios.get('http://localhost:5000/api/agendamentos');
        this.agendamentos = response.data;
      } catch (error) {
        console.error('Erro ao buscar agendamentos:', error);
      }
    },
    async carregarPacientes() {
      try {
        const response = await axios.get('http://localhost:5000/api/pacientes');
        this.pacientes = response.data;
      } catch (error) {
        console.error('Erro ao buscar pacientes:', error);
      }
    },
    async carregarProfissionais() {
      try {
        const response = await axios.get('http://localhost:5000/api/funcionarios');
        this.profissionais = response.data;
      } catch (error) {
        console.error('Erro ao buscar profissionais:', error);
      }
    },
    formatarDataHora(dataHora) {
      const data = new Date(dataHora);
      return data.toLocaleString('pt-BR');
    },
    getPacienteNome(id) {
      const paciente = this.pacientes.find(p => p.id === id);
      return paciente ? paciente.nome : `ID ${id}`;
    },
    getProfissionalNome(id) {
      const profissional = this.profissionais.find(f => f.id === id);
      return profissional ? profissional.nome : `ID ${id}`;
    }
  }
};
</script>
