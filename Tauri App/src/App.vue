<script setup lang="ts">
import Sidebar from "./components/objects/sidebar/Sidebar.vue"
</script>

<!-- Page Container -->
<template class="flex flex-row">

  <!-- Main Page Container -->
  <main class="base">
	<Sidebar navTitle='SOAP'/>	

    <div class="contents">
		<RouterView class='router-view'/>
    </div>

    <!-- <label>
      <input @change="getValue" id="myCheckBox" type="checkbox" />
    </label> -->
  </main>
</template>

<style scoped>

</style>
<style>
:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;

  color: #0f0f0f;
  background-color: #f6f6f6;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

</style>
