<script setup lang="ts">
import {} from "../App.vue"
import PageContainer from "../components/ui/PageContainer.vue"
import Header from "../components/ui/Header.vue"
</script>

<template>
	<Header/>

	<PageContainer>
		<div class='box welcome-box'>
			<div class='title-text'>Welcome to <span class='warning'>SOAP</span></div>
			<p class='sub-text'>hello there, please read the cards below to ensure your best experience with SOAP!</p>
		</div>

		<div class='box backup-box'>
			<p class='title-text'>Make sure to create a system <span class='error'>backup</span></p>
			<p class='sub-text'>Even if you are not applying any “<span style='text-decoration:underline;' class='error'>high risk</span>” tweaks. Even though the tweaks are safe you still want to ALWAYS have a backup.</p>
		</div>

		<div class='box features-box'>
			<p class='title-text'>New Features: <span class='primary'>7.23.0</span> </p>
			<p class='sub-text'></p>
		</div>

		<div class='box color-box'>
			<p class='title-text'>What do the colors on the tweak panels mean?</p>
			<p class='sub-text'>There are different categories ranging from safe to unsafe,
the lower the risk the less likely it is that your system will experience instabilities.</p>

			<p class='color-start primary'>No Risk (Recommended)</p>	
			<p class='color-text'>Will always improve system performance</p>

			<p class='warning'>Low Risk</p>
			<p class='color-text'>Could improve or decrease system performance</p>

			<p class='error'>High Risk</p>
			<p class='color-text'>Has a high chance of breaking the system. </p>


		</div>

		<div class='box'>
			<p class='title-text'>Run SOAP as an <span class='warning'>Administrator</span></p>
			<p class='sub-text'>If you have ran SOAP with default permissions the tweaks will be unable to do anything, so to make sure the tweaks are actually applied: <span style="color:var(--text-active);">Right click on SOAP and click "Run as Administrator"</span>.</p>
		</div>
	</PageContainer>
</template>

<style>
	.box {
		padding: 32px;
		background-color: var(--bg-box);
		border: 1px solid var(--border);

		border-radius: 8px;
		width: 100%;
	}

	.color-box {
grid-row:  span 2;
	}
</style>
