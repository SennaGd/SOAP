import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../pages/home.vue';
import TweakView from '../pages/tweaks.vue';
import DebloatView from '../pages/debloat.vue';


const routes = [
  { path: '/', component: HomeView },
  { path: '/tweaks', component: TweakView },
  { path: '/debloat', component: DebloatView },
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
