import { createApp } from "vue"
import App from "./App.vue"
import { router } from "./router"
import cors from "cors"




createApp(App)
  .use(router)
  .mount("#app")