<script setup>
	import { ref } from 'vue';
	import { computed } from 'vue'
	const props = defineProps({
	  to: { type: [String, Object], required: true }, 
	  title: { type: String, required: true },
	  icon: { type: String, required: true } // Expecting just the filename like 'mouse.svg'
	})
	const iconUrl = computed(() => {
	  return new URL(`../../../icons/${props.icon}`, import.meta.url).href
	})

</script>

<template>
	<RouterLink class='nav-button' :to="to"> 
		<img class='nav-icon' :src="iconUrl"/>
		<div class='nav-text'>{{ title }}</div>
	</RouterLink>	
</template>	
