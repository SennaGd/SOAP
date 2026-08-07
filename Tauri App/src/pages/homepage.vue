<script setup lang="ts">
import {} from "../App.vue"

import HeaderFrame from "../components/ui/HeaderFrame.vue"
import PageContainer from "../components/ui/PageContainer.vue"
</script>

<template>
		<HeaderFrame>
			<h1>SOAP</h1>
			<p>Simple. Obvious. Abstract. Practical.</p>
		</HeaderFrame>
		
		<PageContainer>
			<div class='big-box box'></div>
				<div class='box-container'>
				<div class='small-box box'>
					<p class='sm-sub-title m-margin'>Check out</p>
					<h2 class='sm-title'>Tweaks</h2>
					<RouterLink to='/tweaks' class='sm-button'><p>→</p></RouterLink>
				</div>
				<div class='small-box box'>
					<p class='sm-sub-title m-margin'>Download</p>
					<h2 class='sm-title'>Applications</h2>
					<RouterLink to='/applications' class='sm-button'><p>→</p></RouterLink>
				</div>
			</div>

		</PageContainer>
		</template>
