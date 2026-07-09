<script setup lang="ts">
import { invoke } from "@tauri-apps/api/core"
import {} from "../App.vue"
import data from "../../components/tweaks.json"
import sortTweaksOnCategory from "../../components/fetchTweaks.ts"
import TweakPanel from "../../components/ui/TweakPanel.vue"
const sortedTweaks = sortTweaksOnCategory(data, "input")

</script>

<template class=''>
	<div class='tweak-container'>
		<div v-for="tweak in sortedTweaks">
			<TweakPanel :title=tweak.name :description=tweak.description 
			:tweak=tweak
			/>

		</div>

		
		<!-- One Tweak 
		<TweakPanel 
			title='MouseDataQueueSize'
			description='Reduces the check interval on Mouse inputs.'
		/>
		<TweakPanel 
			title='KeyboardDataQueueSize'
			description='Reduces the check interval on keyboard inputs.'
			/> -->
	</div>
</template>
