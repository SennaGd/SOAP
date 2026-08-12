<script setup lang="ts">
import {} from "../App.vue"
import { TweaksResponse } from "../components/dataclasses/tweakdataclasses"
import PageContainer from "../components/ui/PageContainer.vue"
import HeaderFrame from "../components/ui/HeaderFrame.vue"
import CategoryContainer from "../components/ui/CategoryContainer.vue"
import CategoryBox from "../components/ui/TweakCategory.vue"
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
