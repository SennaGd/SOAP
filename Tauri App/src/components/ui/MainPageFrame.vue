<script setup>
import { ref } from 'vue'
const isEnabled = ref(false)

defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
  }
})
</script>
<template>

	<!-- One Tweak -->
	<div class='tweak-panel'>
		<div class='panel-container'>
			<h2>{{ title }}</h2>
			<p>{{ description }}</p>
		</div>	
		
		<div class='button-container'>
			<label class="switch">
				<input type="checkbox">
				<span class="slider round"></span>
			</label>
		</div>
	</div>	



</template>
