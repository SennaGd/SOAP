import {Tweak, TweaksResponse} from "./dataclasses/tweakdataclasses.ts"

export const tweaks = ref<Tweak[]>([]);

async function fetchTweaks(): Promise<void> {
  try {
    const res = await fetch("/api/v1/tweak/")
    if (!res.ok) throw new Error(`Failed: ${res.status}`)

    const data: TweaksResponse = await res.json()
    tweaks.value = data.tweaks   
  } finally {
    console.log("success!");
  }
}
