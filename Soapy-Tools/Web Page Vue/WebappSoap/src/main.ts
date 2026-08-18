import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Header from './components/Header.vue'
import './style.css'

const app = createApp(App)

app.use(router)
app.component('Header', Header)

app.mount('#app')
