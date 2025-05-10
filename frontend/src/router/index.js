import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/painel',
    name: 'Painel',
    component: () => import('../views/Painel.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/agendamentos',
    name: 'Agendamentos',
    component: () => import('../views/AgendamentoView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView
  },
  {
  path: '/profissionais',
  component: () => import('@/views/ProfissionaisView.vue'),
  meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
