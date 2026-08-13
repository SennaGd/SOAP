<script setup lang='ts'>
		

</script>

<template>
	<div class='page-container'>
		<slot></slot>
	</div>
</template>

<style>
.page-container {
	display: flex;
	flex-direction: column;
	padding-top: 32px;

	padding-bottom: 32px;
	grid-gap: 16px;

	margin: 0 15%;
}

.page-container .sm-box {
	flex: 50%;
}

.page-container .big-box {
	flex: 100%;
}



</style>
