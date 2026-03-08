<!-- frontend/src/components/ui/Inputs/TextInput.vue -->

<template>
  <div class="input-wrapper">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <input
      type="number"
      :value="modelValue"
      @input="handleInput"
      @blur="handleBlur"
      class="form-control"
      :disabled="disabled"
    />
  </div>
</template>

<script setup lang="ts"> 

defineProps<{
    modelValue: string
    disabled?: boolean
}>();


const emit = defineEmits<{
    (e: 'update:modelValue', value: string): void
}>();
const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  emit('update:modelValue', target.value)
}
const handleBlur = (event: Event) => {
    const target = event.target as HTMLInputElement
    emit('update:modelValue', target.value.trim())
}

</script>