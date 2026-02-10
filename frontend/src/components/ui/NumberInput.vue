<!-- frontend/src/components/ui/NumberInput.vue -->

<template>
  <input
    type="number"
    :value="modelValue"
    @input="handleInput"
    @blur="handleBlur"
    class="form-control"
  />
</template>

<script setup lang="ts">
const props = defineProps<{
    modelValue: number | string
}>();

const emit = defineEmits<{
    (e: 'update:modelValue', value: number): void
}>();

const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    // valueAsNumber devuelve un número real o NaN si está vacío
    const val = target.valueAsNumber;
    if (!isNaN(val)) {
        emit('update:modelValue', val);
    }
};

const handleBlur = (event: Event) => {
    const target = event.target as HTMLInputElement;
    // Forzamos la actualización final al salir del foco
    emit('update:modelValue', target.valueAsNumber || 0);
};
</script>

<style>
/* Chrome, Edge, Safari */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield; /* ignore */
}

</style>