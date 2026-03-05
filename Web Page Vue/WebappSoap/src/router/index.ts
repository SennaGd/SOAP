import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/pages/homepage.vue'
import AboutView from '@/pages/aboutpage.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/about', component: AboutView },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
