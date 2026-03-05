<script setup>
  import { ref } from 'vue'

  const toggled = ref(false)

  function Toggle() {
    toggled.value = !toggled.value
    console.log(toggled.value)
  }
</script>

<script>
  export default {
    props: {
      tweakName: String,
      tweakDescription: String
    }
  }
</script>

<template>
  <div class="tweakframe">

    <!-- title -->
    <div class="header"> 
      <h1 id="TweakName">{{tweakName}}</h1> 
    </div>    

    <!-- description -->
    <div class="content"> 
      <p>{{ tweakDescription }}</p>
    </div>    
    <!-- button -->
    <div class="toggle togglebutton">    
      <button @click="Toggle">
        Toggle {{ toggled }}
      </button>     
    </div>    

  </div>
</template>


<style>
.tweakframe {
    background-color: #2c2929 ;

    width: 30vw ;
    height: 25vh ;
    
    border-radius: 15px ;
    border: 2px solid #3b3838 ;

    display: grid ;
    grid-template-areas: 
      "header header"
      "content content"
      "empty toggle" ;
      
    grid-template-columns: 1fr 3fr;
    gap: 3px ;
    padding:15px;
    
}
.tweakframe div.header {
  align-self:end;
  grid-area: header;
  text-align: center;
}

.tweakframe div.content {
  text-align: center;
  grid-area: content;
  text-align: left;
  padding-left: 20px;
  padding-right: 20px;
}

.tweakframe div.toggle {
  grid-area: toggle;
  display: block;
  justify-self: end;
  align-self:end;
}

.title {

}

.description {

}

.togglebutton {
    background-color: red;
}
</style>