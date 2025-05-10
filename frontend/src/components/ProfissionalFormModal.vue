<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h2>{{ profissional.id ? 'Editar' : 'Novo' }} Profissional</h2>
      
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label>Nome*</label>
          <input 
            v-model="form.nome" 
            required
            @blur="v$.nome.$touch()"
            :class="{ 'error': v$.nome.$error }"
          >
          <span v-if="v$.nome.$error" class="error-message">
            {{ v$.nome.$errors[0].$message }}
          </span>
        </div>

        <div class="form-group">
          <label>Especialidade*</label>
          <input 
            v-model="form.especialidade" 
            required
            @blur="v$.especialidade.$touch()"
            :class="{ 'error': v$.especialidade.$error }"
          >
          <span v-if="v$.especialidade.$error" class="error-message">
            {{ v$.especialidade.$errors[0].$message }}
          </span>
        </div>

        <div class="form-group">
          <label>
            <input type="checkbox" v-model="form.ativo">
            Ativo
          </label>
        </div>

        <div class="form-group">
          <label>Foto</label>
          <input type="file" @change="handleFileUpload">
          <img v-if="previewImage" :src="previewImage" class="image-preview">
        </div>

        <div class="form-actions">
          <button type="button" @click="close">Cancelar</button>
          <button type="submit" :disabled="v$.$invalid">
            {{ profissional.id ? 'Atualizar' : 'Salvar' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch, computed } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, minLength } from '@vuelidate/validators'
import { useProfissionalStore } from '@/stores/profissionalStore'

const props = defineProps({
  profissional: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['close', 'save'])

const store = useProfissionalStore()
const previewImage = ref(null)
const selectedFile = ref(null)

const form = reactive({
  nome: '',
  especialidade: '',
  ativo: true
})

const rules = {
  nome: { required, minLength: minLength(3) },
  especialidade: { required }
}

const v$ = useVuelidate(rules, form)

// Preencher form ao editar
watch(() => props.profissional, (prof) => {
  if (prof) {
    form.nome = prof.nome
    form.especialidade = prof.especialidade
    form.ativo = prof.ativo
    previewImage.value = prof.foto_url || null
  } else {
    resetForm()
  }
}, { immediate: true })

const resetForm = () => {
  form.nome = ''
  form.especialidade = ''
  form.ativo = true
  previewImage.value = null
  selectedFile.value = null
  v$.value.$reset()
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    previewImage.value = URL.createObjectURL(file)
  }
}

const close = () => {
  emit('close')
}

const submitForm = async () => {
  const isValid = await v$.value.$validate()
  if (!isValid) return

  try {
    let profissionalData = { ...form }
    
    // Se estiver editando
    if (props.profissional?.id) {
      profissionalData.id = props.profissional.id
    }

    // Chamar a store para salvar
    const savedProfissional = await (profissionalData.id 
      ? store.updateProfissional(profissionalData)
      : store.createProfissional(profissionalData))

    // Upload da foto se existir
    if (selectedFile.value) {
      await store.uploadFoto(savedProfissional.id, selectedFile.value)
    }

    emit('save', savedProfissional)
    close()
  } catch (error) {
    console.error('Erro ao salvar profissional:', error)
  }
}
</script>

<style scoped>
/* Estilos completos disponíveis */
</style>