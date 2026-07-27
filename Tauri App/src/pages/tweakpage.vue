<script setup lang="ts">
import {} from "../App.vue"
import { TweaksResponse } from "../components/dataclasses/tweakdataclasses"
import HeaderFrame from "../components/ui/HeaderFrame.vue"
import CategoryContainer from "../components/ui/CategoryContainer.vue"
import CategoryBox from "../components/ui/TweakCategory.vue"
</script>

<template>
	<HeaderFrame>
		<h1>Tweaks</h1>
		<p>Select a category destination start optimizing.</p>
	</HeaderFrame>

	<CategoryContainer>
		<CategoryBox 
			title='Input Devices' 
			description='Contains tweaks for decreasing the latency between your input devices.'
			destination="/tweaks/inputs"
			/>
			
		<CategoryBox 
			title='Kernel' 
			description='Here you will find tweaks for optimizing the Windows kernel which has a bad prioritization on handling different processes.'
			destination="tweaks/kernel"
			/>
		<CategoryBox 
			title='GPU' 
			description='Here you will find various optimizations for reducing gpu usage on unnecessary gpu usage.'
			destination="/tweaks/gpu"
			/>
		<CategoryBox 
			title='CPU' 
			description='Contains tweaks reducing unnecessary cpu usage and optimizes the cpu’s scheduler destination be the most performant. '
			destination="/tweaks/cpu"
			/>
		<CategoryBox 
			title='Audio' 
			description='Subtle tweaks reducing latency in audio devices.'
			destination="/tweaks/audio"
			/>
		<CategoryBox 
			title='Network' 
			description='This page contains tweaks for decreasing the latency between your input devices.'
			destination="/tweaks/network"
			/>






	</CategoryContainer>
</template>
