<script setup >
import { collapsed, toggleSidebar, sidebarWidth } from './state.js'
import SidebarLink from './sidebarLink.vue'
</script>

<template>
    <div class='sidebar gap-2' :style="{width: sidebarWidth}">
        <h1>
            <span v-if="collapsed">
                <div><h2>SOAP</h2></div>

            </span>
            <span v-else>
                <h2>SOAP</h2>
            </span>
        </h1>

        <SidebarLink to="/" icon="fa-solid fa-soap">Home</SidebarLink>
        <SidebarLink to="/tweaks" icon="fa-solid fa-gears">Tweaks</SidebarLink>
        <SidebarLink to="/debloat" icon="fa-solid fa-screwdriver-wrench">Debloat</SidebarLink>

        <span class="collapse-icon ml-[11.5px]" :class=" { 'rotate-180' : collapsed } " @click="toggleSidebar">
            <i class="fas fa-angle-double-left "></i>
        </span>

    </div>
</template>





<style lang="css" scoped>

.sidebar {
    color: white ;
    background-color: var(--sidebar-bg-color);

    float: left ;
    z-index: 1 ;
    top: 0 ;
    left: 0 ;
    bottom: 0 ;
    padding: 0.5em ;
    height: 100vh ;
    transition: 0.3s ease ;

    display: flex ;
    flex-direction: column ;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
    background-color: transparent ;
    position: absolute ;
    bottom: 0 ;
    left: 0 ;
    padding: 0.75em ;

    color: rgba( 255, 255, 255, 0.7 ) ;

    transition: 0.2s linear ;
}

.rotate-180 {
    transform: rotate( 90 ) ;
    transition: 0.2s linear ;
}

</style>