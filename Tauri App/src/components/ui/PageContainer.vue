<script setup lang='ts'>
		

</script>

<template>
	<div class='page-container'>
		<slot></slot>
	</div>
</template>

<style>
.page-container {
	padding-top: 40px;
	display: flex;
	justify-content: center;
	align-items: center;
	max-width: 1000px;
	margin:auto;
	flex-direction: row;
	gap: 20px;
	flex-wrap: wrap;
}




</style>
