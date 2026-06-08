<script setup lang="ts">
import {} from "../App.vue"
import { TweaksResponse } from "../components/dataclasses/tweakdataclasses"


// const tweaksArray:TweaksResponse = tweaks;
</script>

<template >
    <h1>TweaksPage</h1>
        
    <!-- <div class='background-color:#0a0a0a;'v-for="tweak in tweaksArray">
        <p>Name: {{ tweak.name }}</p>
        <p>Description: {{ tweak.description }}</p>
		</div> -->
	<div class="tweak-page-container">
		<div class="tweak-element ">

			<div class="tweak-element-title col-start-1">
				<h1>Tweak</h1>
			</div>

			<div class="tweak-element-description row-start-2">
				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum nulla at nunc maximus, non consectetur lacus feugiat. Vivamus porttitor porta nibh,sit . </p>
			</div>

			<div class="tweak-element-button row-start-2 col-start-2">
				<button>enable</button>
			</div>
		</div>
		<div class="tweak-element ">
			<div class="tweak-element-title col-start-1">
				<h1>Tweak</h1>
			</div>

			<div class="tweak-element-description row-start-2">
				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum nulla at nunc maximus, non consectetur lacus feugiat. Vivamus porttitor porta nibh,sit . </p>
			</div>

			<div class="tweak-element-button row-start-2 col-start-2">
				<button>enable</button>
			</div>
		</div>
	</div>
    <!-- <label>
      <input @change="getValue" id="myCheckBox" type="checkbox" />
    </label> -->

</template>
