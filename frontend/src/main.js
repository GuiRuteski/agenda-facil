import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'  // Importe o Pinia corretamente
import '@fortawesome/fontawesome-free/css/all.css'

// Crie a instância do app
const app = createApp(App)

// Use o Pinia
const pinia = createPinia()
app.use(pinia)

// Use o router
app.use(router)

// Monte o app
app.mount('#app')