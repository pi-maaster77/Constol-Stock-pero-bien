<!-- frontend/src/components/ui/Inputs/DateInput.vue -->

<script setup lang="ts">
import { ref } from 'vue'

const selectedDate = ref(new Date().toISOString().substr(0, 10)) // Formato YYYY-MM-DD

const props = defineProps<{
  modelValue: string
  disabled?: boolean
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

function update(event: Event) {
  const value = (event.target as HTMLInputElement).value
  emit('update:modelValue', value)
}

function blur(event: Event) {
  const value = (event.target as HTMLInputElement).value.trim()
  emit('update:modelValue', value)
}
</script>

<template>
  <div class="input-wrapper">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <input
      type="date"
      id="moveDate"
      :value="modelValue"
      @input="update"
      @blur="blur"
      class="form-control form-control-sm border-secondary-subtle"
    />
  </div>
</template>
