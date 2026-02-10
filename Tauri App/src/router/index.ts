import { createRouter, createWebHashHistory } from "vue-router"

import HomeView from "../pages/homepage.vue"
import TweaksView from "../pages/tweakpage.vue"
const routes = [
  { path: "/", component: HomeView },
  { path: "/tweaks", component: TweaksView },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
