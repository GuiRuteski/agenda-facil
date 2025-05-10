<template>
  <div class="container">
    <!-- Filtros -->
    <div class="filters">
      <input v-model="filters.especialidade" placeholder="Filtrar por especialidade">
      <select v-model="filters.ativo">
        <option :value="true">Ativos</option>
        <option :value="false">Inativos</option>
        <option :value="null">Todos</option>
      </select>
      <button @click="applyFilters">Aplicar</button>
    </div>

    <!-- Listagem -->
    <table class="profissionais-table">
      <thead>
        <tr>
          <th>Foto</th>
          <th @click="sort('nome')">Nome</th>
          <th @click="sort('especialidade')">Especialidade</th>
          <th>Status</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="prof in profissionais" :key="prof.id">
          <td>
            <img v-if="prof.foto_url" :src="prof.foto_url" class="foto-thumbnail">
            <span v-else>Sem foto</span>
          </td>
          <td>{{ prof.nome }}</td>
          <td>{{ prof.especialidade }}</td>
          <td>
            <span :class="['status-badge', prof.ativo ? 'active' : 'inactive']">
              {{ prof.ativo ? 'Ativo' : 'Inativo' }}
            </span>
          </td>
          <td class="actions">
            <button @click="openEditModal(prof)">Editar</button>
            <button @click="toggleStatus(prof)">
              {{ prof.ativo ? 'Desativar' : 'Ativar' }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Paginação -->
    <div class="pagination">
      <button 
        v-for="page in pageNumbers" 
        :key="page"
        @click="changePage(page)"
        :class="{ active: pagination.page === page }"
      >
        {{ page }}
      </button>
    </div>

    <!-- Modal de Edição -->
    <ProfissionalFormModal
      v-if="showModal"
      :profissional="currentProfissional"
      @close="closeModal"
      @save="handleSave"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useProfissionalStore } from '@/stores/profissionalStore'
import ProfissionalFormModal from '@/components/ProfissionalFormModal.vue'

const store = useProfissionalStore()
const showModal = ref(false)
const currentProfissional = ref(null)
const filters = ref({
  especialidade: '',
  ativo: true
})

// Computed
const profissionais = computed(() => store.profissionais)
const pagination = computed(() => store.pagination)
const pageNumbers = computed(() => {
  const pages = []
  const totalPages = Math.ceil(pagination.value.total / pagination.value.perPage)
  for (let i = 1; i <= totalPages; i++) {
    pages.push(i)
  }
  return pages
})

// Métodos
const fetchData = async () => {
  await store.fetchProfissionais()
}

const openEditModal = (prof = null) => {
  currentProfissional.value = prof
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  currentProfissional.value = null
}

const handleSave = async (profData) => {
  try {
    if (profData.id) {
      await store.updateProfissional(profData)
    } else {
      await store.createProfissional(profData)
    }
    await fetchData()
    closeModal()
  } catch (error) {
    console.error('Erro ao salvar:', error)
  }
}

const toggleStatus = async (prof) => {
  try {
    await store.updateProfissional({
      ...prof,
      ativo: !prof.ativo
    })
    await fetchData()
  } catch (error) {
    console.error('Erro ao alterar status:', error)
  }
}

const applyFilters = () => {
  store.filters = filters.value
  fetchData()
}

const changePage = (page) => {
  store.pagination.page = page
  fetchData()
}

// Inicialização
onMounted(fetchData)
</script>

<style scoped>
/* Estilos completos no GitHub */
</style>