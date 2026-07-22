<script setup>
import { invoke } from "@tauri-apps/api/core";
import { ref, toRefs, computed, onMounted } from 'vue'
import { writeTextFile, BaseDirectory } from '@tauri-apps/plugin-fs';
import { load } from '@tauri-apps/plugin-store'

const props = defineProps({
  title: {type: String, required: true},
  description: {type: String},
  tweak: {type: Object}
})

const { tweak } = toRefs(props)
const tweakObj = Object.values(tweak)

const isChecked = ref(false)
const componentId = tweakObj[0].tweak.name 

let store = null
onMounted(async () => {
  // Asynchronously load the store to establish the resource ID
  store = await load('soap-button-states.json')
  
  const savedState = await store.get(componentId)
  if (savedState !== null) {
    isChecked.value = Boolean(savedState)
  }
})

async function handleToggle() {
  if (store) {
    await store.set(componentId, isChecked.value ? 1 : 0)
	await store.save()
	console.log(isChecked.value)
  }
}

// applies all registry edits inside one tweak
function applyTweaks() {
	for (var x = 0; x < tweakObj[0].tweak.apply.length; x++) {
		var current_tweak= tweakObj[0].tweak.apply[x] // x of many apply tweaks

//		invoke("key_handler", {
//			function: current_tweak.function,
//			hive: current_tweak.hive,
//			path: current_tweak.path,
//			keyName: current_tweak.name,
//			keyValue: current_tweak.value
//		})

		console.log("applied", componentId)
	}

}

// reverts all registry edits inside one tweak
function revertTweaks() {
	for (var x = 0; x < tweakObj[0].tweak.revert.length; x++) {
		var current_tweak = tweakObj[0].tweak.revert[x] // x of many apply tweaks

//		invoke("key_handler", {
//			function: current_tweak.function,
//			hive: current_tweak.hive,
//			path: current_tweak.path,
//			keyName: current_tweak.name,
//			keyValue: current_tweak.value
//		})


		console.log("reverted", componentId);
	}
}

const toggleTweak = computed(() => {
	return isChecked.value ? 
	applyTweaks() : revertTweaks()
})

</script>


<template>

	<!-- One Tweak -->
	<div class='tweak-panel'>
		<div class='panel-container'>
			<h2>{{ title }}</h2>
			<p>{{ description }}</p>
			<label for='checkbox'>{{toggleTweak}}</label>	
		</div>	
		
		<div class='button-container'>
			<label class="switch">
				<input  type="checkbox" v-model="isChecked" @change="handleToggle">
				<span class="slider round"></span>
			</label>
		</div>
	</div>	



</template>
