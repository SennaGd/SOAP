<script setup lang="ts">
import {} from "../App.vue"
import HeaderFrame from "../components/ui/HeaderFrame.vue"
import PageContainer from "../components/ui/PageContainer.vue"
import CategoryContainer from "../components/ui/CategoryContainer.vue"
</script>

<template>
	<HeaderFrame>
		<h1>Applications</h1>
		<p>Download applications that you need here.</p>
	</HeaderFrame>

	<PageContainer>
			<div class='big-box box'>
				<h2 class='sm-title'>Applications are currently not working..</h2>
				<p class='sm-sub-title sm-margin'>Check out the Tweak or Automation page.</p>
				<div class='row-container m-margin'>
					<RouterLink to='/tweaks' class='sm-button sm-text'> 
						<p>Tweaks</p>
					</RouterLink>

					<RouterLink to='/applications' class='sm-button sm-text'>
						<p>Automation</p>
					</RouterLink>
				</div>
			</div>
	</PageContainer>
</template>
