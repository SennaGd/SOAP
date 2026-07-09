import { createRouter, createWebHashHistory } from "vue-router"
import { 
	HomeView, 
	TweaksView, 
	PrivacyView, 
	AppView, 
	SettingsView, 
	AutomationView,

	InputTweaks,
	KernelTweaks,
	CPUTweaks,
	GPUTweaks,
	NetworkTweaks,
	AudioTweaks

} from "../pages"

const routes = [
 { path: "/", component: HomeView },
 { path: "/tweaks", component: TweaksView },

 { path: "/tweaks/inputs", component: InputTweaks},
 { path: "/tweaks/gpu", component: GPUTweaks},
 { path: "/tweaks/cpu", component: CPUTweaks},
 { path: "/tweaks/kernel", component: KernelTweaks},
 { path: "/tweaks/network", component: NetworkTweaks},
 { path: "/tweaks/audio", component: AudioTweaks},
 
 { path: "/privacy", component: PrivacyView },
 { path: "/apps", component: AppView },
 { path: "/settings", component: SettingsView},
 { path: "/automation", component: AutomationView},
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
