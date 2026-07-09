<script setup lang='ts'>
		

</script>

<template>
	<div class='category-container'>
		<slot></slot>
	</div>
</template>

<style>
.category-container {
	padding-top: 40px;
	margin:auto;
	margin-top: 20px;
	display: grid;
	width: 850px;
	gap: 40px 50px;
	grid-template-columns: 1fr 1fr;
	overflow: auto;
}


</style>
