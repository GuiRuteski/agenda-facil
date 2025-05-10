import { defineStore } from 'pinia';
import api from '@/services/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),
  actions: {
    async login(credentials) {
      const response = await api.post('/api/auth/login', credentials);
      this.token = response.data.access_token;
      localStorage.setItem('token', this.token);
      await this.fetchUser();
    },
    async fetchUser() {
      const response = await api.get('/api/auth/me');
      this.user = response.data;
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('token');
    },
  },
});