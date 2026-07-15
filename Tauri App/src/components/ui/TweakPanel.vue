<script setup>
import { invoke } from "@tauri-apps/api/core";
import { ref, toRefs, computed } from 'vue'

const isEnabled = ref(false)

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
  },

  tweak: {
	type: Object,
  }
})

const { tweak } = toRefs(props)
const tweakObj = Object.values(tweak)

// applies all registry edits inside one tweak
function applyTweaks() {
	for (var x = 0; x < tweakObj[0].tweak.apply.length; x++) {
		var current_tweak= tweakObj[0].tweak.apply[x] // x of many apply tweaks
		//invoke("key_handler", {
			//function: current_tweak.function,
			//hive: current_tweak.hive, 
			//path: current_tweak.path,
			//key_name: current_tweak.name,
			//key_value: current_tweak.value

		//})
		invoke("key_handler", {
			function: current_tweak.function,
			hive: current_tweak.hive,
			path: current_tweak.path,
			keyName: current_tweak.name,
			keyValue: current_tweak.value
		})

		console.log(current_tweak)
	}
}

// reverts all registry edits inside one tweak
function revertTweaks() {
	for (var x = 0; x < tweakObj[0].tweak.revert.length; x++) {
		var current_tweak = tweakObj[0].tweak.revert[x] // x of many apply tweaks
		// invoke("key_handler", {
		// 	function: current_tweak.function,
		// 	hive: current_tweak.hive, 
		// 	path: current_tweak.path,
		// 	key_name: current_tweak.name,
		// 	key_value: current_tweak.value
		// })
		invoke("key_handler", {
			function: current_tweak.function,
			hive: current_tweak.hive,
			path: current_tweak.path,
			keyName: current_tweak.name,
			keyValue: current_tweak.value
		})


		console.log(current_tweak);
	}
}

// responsible for toggling tweaks (communicates to back-end)
const toggleTweak = computed(() => {
	return isEnabled.value ? 
		applyTweaks() : 
		revertTweaks()
})

// var command = invoke("hello", { title: "senna"});

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
				<input type="checkbox" v-model='isEnabled'>
				<span class="slider round"></span>
			</label>
		</div>
	</div>	



</template>
