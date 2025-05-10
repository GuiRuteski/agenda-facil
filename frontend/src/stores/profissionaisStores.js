import { defineStore } from 'pinia'
import api from '@/services/api'

export const useProfissionalStore = defineStore('profissionais', {
  state: () => ({
    profissionais: [],
    loading: false,
    pagination: {
      page: 1,
      perPage: 10,
      total: 0
    },
    filters: {
      especialidade: '',
      ativo: true
    }
  }),
  actions: {
    async fetchProfissionais() {
      this.loading = true
      try {
        const params = {
          page: this.pagination.page,
          per_page: this.pagination.perPage,
          ...this.filters
        }
        
        const response = await api.get('/profissionais', { params })
        this.profissionais = response.data.items
        this.pagination.total = response.data.total
      } catch (error) {
        console.error('Erro ao buscar profissionais:', error)
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async createProfissional(profissional) {
      try {
        const response = await api.post('/profissionais', profissional)
        this.profissionais.unshift(response.data)
        return response.data
      } catch (error) {
        console.error('Erro ao criar profissional:', error)
        throw error
      }
    },
    
    async uploadFoto(id, file) {
      const formData = new FormData()
      formData.append('foto', file)
      
      try {
        const response = await api.post(`/profissionais/${id}/foto`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        return response.data
      } catch (error) {
        console.error('Erro no upload:', error)
        throw error
      }
    }
  }
})