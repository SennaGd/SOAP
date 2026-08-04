<script setup lang="ts">
import { ref } from "vue";
import { invoke } from "@tauri-apps/api/core";
import Sidebar from "./components/objects/sidebar/Sidebar.vue"
const greetMsg = ref("");
const name = ref("");

const hive = ref("");
const path = ref("");
const tweak_name = ref("");
const tweak_value = ref<string | number>("");

async function greet() {
  // Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
  greetMsg.value = await invoke("greet", { name: name.value });
}

async function manage_registry() {
  // Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
    greetMsg.value = await invoke("manage_registry", {  hive: hive.value, 
                                                        path: path.value,
                                                        name: tweak_name.value,
                                                        value: tweak_value.value
                                                    });
}  

function getValue(event: Event) {
  const isChecked = (event.target as HTMLInputElement).checked;

  if (isChecked) {
        console.log("Input is checked");
        name.value = "hi";
  } else {
        name.value = "hi";
        console.log("Input is NOT checked");
  }
}
</script>

<!-- Page Container -->
<template class="flex flex-row">

  <!-- Main Page Container -->
  <main class="base">
	<Sidebar navTitle='SOAP'/>	

    <div class="contents">
		<RouterView class='router-view'/>
    </div>

    <!-- <label>
      <input @change="getValue" id="myCheckBox" type="checkbox" />
    </label> -->
  </main>
</template>

<style scoped>

</style>
<style>
:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;

  color: #0f0f0f;
  background-color: #f6f6f6;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

</style>
