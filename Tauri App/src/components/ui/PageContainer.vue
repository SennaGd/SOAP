<script setup lang='ts'>
		

</script>

<template>
	<div class='page-container'>
		<slot></slot>
	</div>
</template>

<style>
.page-container {
	display: grid;

	padding-top: 32px;
	grid-gap: 16px;

	margin: 0 15%;
	
	grid-auto-rows: 200px;
	grid-template-columns: repeat(auto-fit,minmax(clamp(100%/3 + 0.1%,(1600px - 100vw)*1000,100%),1fr));
}




</style>
