<script setup>
	import { ref } from 'vue';
	import NavButton from "./NavButton.vue";
	const isEnabled = ref(false);

	defineProps({
	  navTitle: {
		type: String,
		required: true
	  },
	  description: {
		type: String,
	  }
	});

</script>

<template>
	<nav class="sidebar ">
		<div class='nav-title'>
			{{ navTitle }}	
			<img class='collapse-icon' srcset='../../../icons/sidebar-close.svg'/>
		</div>

		<div class="nav-line"><hr/></div>

		<div class='nav-button-group'>
			<NavButton title='Home' to='/' icon='home.svg'/>
			<NavButton title='Tweaks' to='/tweaks/inputs' icon='list.svg'/>
			<NavButton title='Applications' class='disabled' to='/apps' icon='box.svg'/>
		</div>

		<div class="nav-line"><hr/></div>
		
		<div class='nav-button-group'>
			<NavButton title='Automation' class='disabled' to='/automation' icon='save.svg'/>
		</div>

		<div class='nav-button-group'>
			<NavButton title='Privacy' to='/privacy' class='disabled' icon='lock.svg'/>
			<NavButton title='Settings' to='/settings' class='disabled' icon='settings.svg'/>
		</div>
	</nav>
</template>
