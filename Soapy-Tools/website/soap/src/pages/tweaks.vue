<script setup>
    import TweakContainer from '@/components/tweak_item/tweakcontainer.vue'
    import TweakFrame from '@/components/tweak_item/tweakframe.vue'
    import tweaks from "@/components/tweak_item/tweaks.json";

    console.log(Object.keys(tweaks).length);


</script>

<template>
    <TweakContainer>
        <div v-for="tweak in tweaks">
            <TweakFrame :tweakName=tweak[0].name  tweakDescription="This tweak will do .... and provide less queue time for .... which reduces latency and increases fps. "/>
        </div>
        <!-- <TweakFrame tweakName="Tweak 1" tweakDescription="This tweak will do .... and provide less queue time for .... which reduces latency and increases fps. "/>
        <TweakFrame tweakName="Tweak 2" tweakDescription="This tweak will do .... and provide less queue time for .... which reduces latency and increases fps. "/> -->
    </TweakContainer>
</template>