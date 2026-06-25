<script setup lang="ts">
import { ref } from "vue";
import { invoke } from "@tauri-apps/api/core";
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
	
	<!-- Sidebar Panel -->
	<nav class="sidebar ">
		<div class='nav-title'>
			SOAP
			<img class='collapse-icon' srcset='./icons/home.svg'/>
		</div>

		<div class="nav-line"><hr/></div>
		
		<div class='nav-button-group'>
			<RouterLink class='nav-button' to='/'> 
				<img class='nav-icon' srcset='./icons/home.svg'/>
				<div class='nav-text'>Home</div>
			</RouterLink>	
		
			<RouterLink class='nav-button' to='/tweaks'> 
				<img class='nav-icon' srcset='./icons/list.svg'/>
				<div class='nav-text'>Tweaks</div>
			</RouterLink>	
			
			<RouterLink class='nav-button' to='/apps'> 
				<img class='nav-icon' srcset='./icons/box.svg'/>
				<div class='nav-text'>Applications</div>
			</RouterLink>	
		</div>

		<div class='nav-line'><hr/></div>

		<div class='nav-button-group'>
			<RouterLink class='nav-button' to='/automation'> 
				<img class='nav-icon' srcset='./icons/save.svg'/>
				<div class='nav-text'>Automation</div>
			</RouterLink>	

		</div>
		

		<!-- Bottom buttons-->
			<div class='nav-button-group'>
				<RouterLink class='nav-button' to='/privacy'> 
					<img class='nav-icon' srcset='./icons/lock.svg'/>
					<div class='nav-text'>Privacy</div>
				</RouterLink>	

				<RouterLink class='nav-button' to='/settings'> 
					<img class='nav-icon' srcset='./icons/settings.svg'/>
					<div class='nav-text'>Settings</div>
				</RouterLink>	

			</div>

	</nav>
	 
    <div class="contents">
      <RouterView class=''/>
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
