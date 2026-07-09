<script setup lang='ts'>
		

</script>

<template>
	<div class='header-frame'>
		<slot></slot>
	</div>
</template>

<style>
.header-frame {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 100%;
}	

.header-frame h1 {
	font-size: 2.5rem;
	color: var(--text-title);

	display: flex;
	height: 5rem;
	align-items: center;
	font-size: 5rem;	
	font-weight: 700;
	padding-bottom:1rem;
}
.header-frame p {
	font-size: 1.5rem;
	letter-spacing: 5%;
}

</style>
