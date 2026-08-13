<template>
	<div class='header'>
		<div class='header-button soapy-button'>This is so .. 
			<div class="primary">Soapy</div>?
		</div>
		
		<slot class='header-button header-centered'>
			
		</slot>

		<div class='header-button soapy-version'>Version: 
			<div class='primary'> 7.23.0</div> 
		</div>	
	</div>
</template>

<style>
	.header{
		display: grid;
		grid-template-columns: 1fr 3fr 1fr;
		height: 80px;	
		gap:4px;
		border-bottom: 1px solid var(--border);
	}

	.header-button {
		display: flex;

		background-color: var(--header-button);

		font-size: 14px;

		border: 1px solid var(--border);
		border-radius: 8px;

		padding: 6px 16px;

		margin-top: auto;
		margin-bottom: auto;
		gap: 5px;
	}

	.soapy-button {
		min-width: 170px;
		margin-right:auto;
		margin-left: 32px;
		grid-column: 1;
	}

	.soapy-version {
		min-width: 130px;
		margin-left: auto;
		margin-right: 32px;
		grid-column: 3;
	}

	.category-contaier {
		display: flex;
		flex-direction: row;
		gap: 10px;
		align-items: center;
		justify-content:center;

	}
	.category-button {
		justify-content:center;
		width: 100px;
	}


</style>

