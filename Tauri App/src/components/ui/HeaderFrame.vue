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
	font-family: system-ui;
	padding-top: 5rem;
	display: flex;
	font-weight: bold;
	
	height: 5rem;
	align-items: center;
	font-size: 110px;	
	padding-bottom:2.5rem;
}
.header-frame p {
	padding-top: 1rem;
	padding-bottom: 2rem;
	font-size: 24px;
	letter-spacing: 5%;
}

.title-frame {
	display: flex;
	flex-direction: row;
	gap: 1.5rem;
}
.soap-title {
	color: var(--text-title);
}

.welcome-title {
}

</style>
