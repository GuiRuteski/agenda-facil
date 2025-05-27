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
    path: '/home',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'),
    meta: { requiresAuth: true }
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
  {
    path: '/settings/account',
    name: 'AccountSettings',
    component: () => import('@/views/settings/AccountSettingsView.vue')
  },
  {
    path: '/settings/notification',
    name: 'NotificationSettings',
    component: () => import('@/views/settings/NotificationSettingsView.vue')
  },
  {
    path: '/settings/preferences',
    name: 'PreferecesSettings',
    component: () => import('@/views/settings/PreferencesSettingsView.vue')
  },
  {
    path: '/settings/payment',
    name: 'PaySettings',
    component: () => import('@/views/settings/PaySettingsView.vue')
  },
  {
    path: '/settings/support',
    name: 'SupportSettings',
    component: () => import('@/views/settings/SupportSettingsView.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

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
