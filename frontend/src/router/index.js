import { createRouter, createWebHistory } from 'vue-router'

// Importa as views criadas
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import HomeView from '../views/HomeView.vue';

// Aqui futuramente podemos importar o Painel (dashboard) e outras rotas protegidas



const routes = [
  {
    path: '/',
    redirect: '/login' // Redireciona para o login como rota padrão
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
  // Exemplo futura rota protegida
  {
    path: '/painel',
    name: 'Painel',
    component: () => import('../views/Painel.vue'),
    meta: { requiresAuth: true }
  },

  { path: '/', component: LoginView },
  { path: '/register', component: RegisterView },
  { path: '/home', component: HomeView }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Middleware de proteção de rotas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router