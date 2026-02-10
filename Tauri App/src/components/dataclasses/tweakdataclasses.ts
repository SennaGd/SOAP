export type Tweak = {
  id: number
  tweak_function: number
  tweak_path: string
  tweak_key: string
  tweak_type: number
  tweak_value: string
  tweak_id: string
}

export type TweaksResponse = {
  tweaks: Tweak[]
}