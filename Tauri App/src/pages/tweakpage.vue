<script setup lang="ts">
import {} from "../App.vue"
import { TweaksResponse } from "../components/dataclasses/tweakdataclasses"


// const tweaksArray:TweaksResponse = tweaks;
</script>

<template>
    <h1>TweaksPage</h1>
        
    <!-- <div class='background-color:#0a0a0a;'v-for="tweak in tweaksArray">
        <p>Name: {{ tweak.name }}</p>
        <p>Description: {{ tweak.description }}</p>
    </div> -->
    <div class="grid grid-cols-3 gap-4">
        <div class="col-start-1">
            <h1>Tweak</h1>
        </div>

        <div class="col-start-3">
            <p>Description</p>
        </div>

        <div class="col-start-2">
            <button></button>
        </div>
    </div>
    <!-- <label>
      <input @change="getValue" id="myCheckBox" type="checkbox" />
    </label> -->

</template>