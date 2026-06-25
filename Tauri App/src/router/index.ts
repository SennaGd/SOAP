import { createRouter, createWebHashHistory } from "vue-router"

import HomeView from "../pages/homepage.vue"
import TweaksView from "../pages/tweakpage.vue"
import PrivacyView from "../pages/privacypage.vue"
import AppView from "../pages/applicationpage.vue"
import SettingsView from "../pages/settingspage.vue"
import AutomationView from "../pages/automationpage.vue"

const routes = [
 { path: "/", component: HomeView },
 { path: "/tweaks", component: TweaksView },
 { path: "/privacy", component: PrivacyView },
 { path: "/apps", component: AppView },
 { path: "/settings", component: SettingsView},
 { path: "/automation", component: AutomationView},
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
