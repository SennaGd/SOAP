<script setup lang="ts">
const sortedTweaks = sortTweaksOnCategory(data, "gpu")

import data from "../../components/tweaks.json"
import sortTweaksOnCategory from "../../components/fetchTweaks.ts"
import TweakPanel from "../../components/ui/TweakPanel.vue"
import PageContainer from "../../components/ui/PageContainer.vue"

import TweakHeader from "../../components/ui/TweakHeader.vue"

</script>

<template class=''>
	<TweakHeader/>

	<PageContainer>
		<div class='tweak-grid'>	
			<TweakPanel v-for="tweak in sortedTweaks" 
			:title=tweak.name 
			:description=tweak.description 
			:tweak_status=tweak.status
			:tweak=tweak
			/>
		</div>
	</PageContainer>
</template>


