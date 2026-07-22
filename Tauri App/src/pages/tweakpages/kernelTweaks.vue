<script setup lang="ts">
import data from "../../components/tweaks.json"
import sortTweaksOnCategory from "../../components/fetchTweaks.ts"
import TweakPanel from "../../components/ui/TweakPanel.vue"

const sortedTweaks = sortTweaksOnCategory(data, "kernel")
</script>

<template class=''>
	<div class='tweak-container'>
		
		<div v-for="tweak in sortedTweaks">
			<TweakPanel 
				:title=tweak.name 
				:description=tweak.description 
				:tweak=tweak
			/>
		</div>
	</div>
</template>
