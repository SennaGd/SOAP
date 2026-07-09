<script setup lang='ts'>
import { ref } from 'vue'	
import NavButton from "../objects/sidebar/NavButton.vue"
const props = defineProps({
	title: {
		type: String,
		required: true
	},
	description: {
		type: String,
		required: true
	},
	destination: {
		type: String,
		required: true
	}


});
</script>

<template>
	<div class='category-box'>
		<h2>{{ title }}</h2>
		<p>{{description}}</p>
	
		<RouterLink class='link' :to='destination'><p>→</p></RouterLink>
	</div>
</template>

<style>
.category-box {
	background-color: var(--bg-box);

	display: flex;
	flex-direction: column;

	align-items: center;
	text-align: center;
	width: 400px;
	height: 220px;
	padding: 1.5rem;
	gap: 0.5rem;
	padding: 1.75rem 2rem 1.75rem 2rem;

	border-radius: 1rem;
	border: 1px solid var(--border);
}
.link-box {
	margin-top: auto;
}
.category-box h2 {
	color: var(--text-mashed);
	font-size: 2rem;
	font-weight: bold;
}

.category-box p {
	color: var(--sm-sub);
	font-size: 1rem;
}

.link {
	background-color: var(--bg-link-button);

	width: 120px;
	height: 40px;
	border-radius: 8px;

	display: flex;
	font-size: 3rem;
	margin-top: auto;	
}

.link p {
	color: white;
	font-size: 2.75rem;
	text-align: center;

	width: 100%;

	padding-top: 0; 
}
</style>
