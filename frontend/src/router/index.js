import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/RegisterView.vue')
  },
  {
    path: '/painel',
    name: 'Painel',
    component: () => import('../views/Painel.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/scheduling',
    name: 'Scheduling',
    component: () => import('@/views/SchedulingView.vue')
  },
  {
    path: '/professional',
    name: 'Professional',
    component: () => import('@/views/ProfessionalView.vue')
  },
  {
    path: '/patient',
    name: 'Patient',
    component: () => import('@/views/PatientView.vue')
  },
  {
    path: '/message',
    name: 'Message',
    component: () => import('@/views/MessageView.vue')
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('@/views/SettingsView.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 🔐 Middleware global para proteger rotas que exigem login
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const token = localStorage.getItem('token')

  if (requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
