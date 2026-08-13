<script lang='ts' setup>
	import Header from "./Header.vue"

</script>
<template>
	<Header>
		<div class='category-contaier'>
			<RouterLink class='category-button header-button' to="/tweaks/inputs">Input</RouterLink>
			<RouterLink class='category-button header-button' to="/tweaks/cpu">CPU/GPU</RouterLink>
			<RouterLink class='category-button header-button' to="/tweaks/kernel">Kernel</RouterLink>
		</div>
	</Header>
</template>

<style>

</style>

