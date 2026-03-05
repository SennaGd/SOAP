<script setup>
  import Sidebar from "./components/sidebar/sidebar.vue";
</script>


<template>
  
  <main class="main flex flex-row">
    <Sidebar/>
    <div class='routerview flex flex-col  ml-auto mr-auto p-5'>
      <RouterView />
    </div>
  </main>
</template>

<style>
  :root {
    --main-background: #222020 ;
    --sidebar-bg-color: #2D2B2B ;
    --sidebar-item-hover: #353333 ;
    --sidebar-item-active: #1E1D1D ;
  }

  h1 {
    font-size: xx-large;
  }

  h2 {
    font-size: x-large;
  }

  p {
    font-size: large;
  }

  body {
    background-color: var(--main-background);
  }
</style>

<style scoped>
  .main {
    background-color: var(--main-background);
    color:white;
  }
</style>
