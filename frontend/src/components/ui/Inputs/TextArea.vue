<!-- frontend/src/components/ui/Inputs/TextArea.vue -->

<template>
  <div class="input-wrapper">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <textarea
      :value="modelValue"
      @input="update"
      @blur="blur"
      class="form-control"
      :disabled="disabled"
    ></textarea>
  </div>
</template>

<script setup lang="ts">
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
