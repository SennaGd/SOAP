<script setup>
import { ref } from 'vue';
import { computed } from 'vue'
import NavButton from "./NavButton.vue"
const props = defineProps({
  to: { type: [String, Object], required: true }, 
  title: { type: String, required: true },
  icon: { type: String, required: true } 
})

</script>

<template>
	<div class='dropdown'>
		<NavButton class='dropbtn' title='Tweaks' to='/tweaks' icon='list.svg'/>

		<div class='dropdown-content'>
			<RouterLink class='' to="/tweaks/inputs"> 
				<div class='nav-text'>Mouse & Keyboard</div>
			</RouterLink>	
			<RouterLink class='' to="/tweaks/gpu"> 
				<div class='nav-text'>GPU</div>
			</RouterLink>	
			<RouterLink class='' to="/tweaks/cpu"> 
				<div class='nav-text'>CPU</div>
			</RouterLink>
			<RouterLink class='' to="/tweaks/kernel"> 
				<div class='nav-text'>Kernel</div>
			</RouterLink>	
			<RouterLink class='' to="/tweaks/network"> 
				<div class='nav-text'>Network</div>
			</RouterLink>	
			<RouterLink class='' to="/tweaks/audio"> 
				<div class='nav-text'>Audio</div>
			</RouterLink>
		</div>
	</div>
</template>

<style>
.dropdown {	position: relative; transition: 2s;}

.dropbtn nav-button { width: 100%;}
.dropbtn {
	display:relative;
	z-index: 2;
	background-color: var(--bg-sidebar-button);
	border-radius: 8px;
	height: 4rem;
	gap:0.5rem;
}

.dropdown-content {
	z-index: 1;
	display: none;
	position: absolute;
	background-color: var(--bg-dropdown);
	min-width: 200px;
	box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);

	border-radius: 0px 0px 10px 10px;
	top: 1rem;
	padding-top: 2rem;
}

/* Links inside dropdown content */
.dropdown-content a {
	text-align: start;
	color: var(--sm-sub);
	padding: 0.1rem 0.25rem;
	padding-left: 1rem;
	font-size: 0.9rem;
	text-decoration: none;
	display: block;
}

.dropdown-content a:hover {
	transition: 0.2s;
	color: var(--text-mashed);
}
/* Change color of dropdown links on hover */

/* Show the dropdown content on hover */
.dropdown:hover .dropdown-content {
  display: inherit;
}

/* Change background color of dropdown button on hover */
.dropdown:hover .dropbtn {
	background-color: var(--bg-sidebar-button-hover);
}
</style>
