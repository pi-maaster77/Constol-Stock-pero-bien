<!-- frontend/src/components/ui/NumberInput.vue -->

<template>
  <input
    type="number"
    :value="modelValue"
    :step="mode === 'float' ? 'any' : 1"
    @input="handleInput"
    @blur="handleBlur"
    class="form-control"
  />
</template>

<script setup lang="ts">
const props = withDefaults(defineProps<{
    modelValue: number
    mode?: 'int' | 'float'
}>(), {
  mode: 'int'
});

const emit = defineEmits<{
    (e: 'update:modelValue', value: number): void
}>();

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value

  if (props.mode === 'int') {
    value = value.replace(/[^0-9-]/g, '')
    value = value.replace(/(?!^)-/g, '') // solo un - al inicio
  } else {
    value = value.replace(/[^0-9.-]/g, '')
    value = value.replace(/(?!^)-/g, '') // solo un -
    value = value.replace(/(\..*)\./g, '$1') // solo un punto
  }

  target.value = value

  const num = Number(value)
  if (!isNaN(num)) {
    emit('update:modelValue', props.mode === 'int' ? Math.trunc(num) : num)
  }
}

const handleBlur = (event: Event) => {
  const target = event.target as HTMLInputElement;
  let value = target.value

  if (props.mode === 'int') {
    value = value.replace(/[^0-9-]/g, '')
    value = value.replace(/(?!^)-/g, '') // solo un - al inicio
  } else {
    value = value.replace(/[^0-9.-]/g, '')
    value = value.replace(/(?!^)-/g, '') // solo un -
    value = value.replace(/(\..*)\./g, '$1') // solo un punto
  }

  target.value = value

  const num = Number(value)
  if (!isNaN(num)) {
    emit('update:modelValue', props.mode === 'int' ? Math.trunc(num) : num)
  } else {
    emit('update:modelValue', 0)
  }
};

function normalize(value: string | number): number {
    let num = typeof value === 'string'
        ? Number(value)
        : value

    if (isNaN(num)) return 0

    if (props.mode === 'int') {
        return Math.trunc(num)
    }

    return num
}
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
  -moz-appearance: textfield;
  appearance: textfield;
}

</style>