<template>
  <div class="agendamento-view">
    <h1>Gerenciar Agendamentos</h1>
    
    <section>
      <AgendamentoForm />
    </section>

    <hr />

    <section>
      <AgendamentoList />
    </section>
  </div>
</template>

<script>
import AgendamentoForm from '@/components/AgendamentoForm.vue'
import AgendamentoList from '@/components/AgendamentoList.vue'

export default {
  name: 'AgendamentoView',
  components: {
    AgendamentoForm,
    AgendamentoList
  }
}
</script>

<style scoped>
.agendamento-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

section {
  margin-bottom: 30px;
}
</style>
