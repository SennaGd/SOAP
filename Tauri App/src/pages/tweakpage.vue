<script setup lang="ts">
import {} from "../App.vue"
import PageContainer from "../components/ui/PageContainer.vue"
import TweakHeader from "../components/ui/TweakHeader.vue"
</script>

<template>
	<TweakHeader/>
	<PageContainer>

	<div class='box centered-text'>
		<p class='title-text'>Click on an category</p>
		<p class='sub-text'>To view the tweaks</p>
	</div>
	</PageContainer>
</template>

<style>
	.centered-text {
		text-align:center;
	}
</style>
