<!-- frontend/src/components/ui/Inputs/NumberInputWithButtons.vue -->

<template>
  <div class="input-wrapper">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <span class="input-group">
      <NumberInput :modelValue="modelValue" @update:modelValue="change" />
      <ButtonAdd @click="increment" />
      <ButtonDecrement @click="decrement" />
    </span>
  </div>
</template>

<script setup lang="ts">
import ButtonDecrement from '../Buttons/ButtonDecrement.vue'
import ButtonAdd from '../Buttons/ButtonAdd.vue'
import NumberInput from './NumberInput.vue'

defineProps<{
  modelValue: string | null
  mode?: 'int' | 'float'
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: number): void
  (e: 'increment'): void
  (e: 'decrement'): void
}>()
function increment() {
  emit('increment')
}

function decrement() {
  emit('decrement')
}

// 2. El evento que viene de NumberInput ya es el valor, no el objeto Event
function change(value: string | null) {
  emit('update:modelValue', Number(value))
}
</script>
