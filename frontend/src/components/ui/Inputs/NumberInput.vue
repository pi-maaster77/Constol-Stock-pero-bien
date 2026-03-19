<!-- frontend/src/components/ui/Inputs/NumberInput.vue -->

<template>
  <div class="input-wrapper" v-if="$slots.label">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <input
      :type="props.mode === 'barcode' ? 'text' : 'number'"
      :value="modelValue"
      :step="mode === 'float' ? 'any' : 1"
			:disabled="disabled"
      @input="handleInput"
      @blur="handleBlur"
      class="form-control"
    />
  </div>
  <input
    v-else
    :type="props.mode === 'barcode' ? 'text' : 'number'"
    :value="modelValue"
    :step="mode === 'float' ? 'any' : 1"
		:disabled="disabled"
    @input="handleInput"
    @blur="handleBlur"
    class="form-control"
  />
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    // Aceptamos ambos tipos para que no de error en CreateEditProduct
    modelValue: string | number | null
    mode?: 'int' | 'float' | 'barcode'
		disabled?: boolean
  }>(),
  {
    mode: 'int',
  },
)

const emit = defineEmits<{
  (e: 'update:modelValue', value: string | null): void
}>()

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value

  if (props.mode === 'barcode') {
    // IMPORTANTE: En barcode tratamos TODO como string puro
    value = value.replace(/[^0-9]/g, '')
    if (value.length > 20) value = value.slice(0, 20)

    target.value = value
    emit('update:modelValue', value) // Emitimos el string tal cual (con ceros)
    return
  }

  // Lógica para números (int / float)
  if (props.mode === 'int') {
    value = value.replace(/[^0-9-]/g, '')
    value = value.replace(/(?!^)-/g, '')
  } else if (props.mode === 'float') {
    value = value.replace(/[^0-9.-]/g, '')
    value = value.replace(/(?!^)-/g, '')
    value = value.replace(/(\..*)\./g, '$1')
  }

  target.value = value

  // Solo convertimos a Number para validar que es un número válido,
  // pero si el usuario está escribiendo (ej: "1."), no emitimos el Number(value)
  // porque "1." se convertiría en "1", impidiendo escribir decimales.
  emit('update:modelValue', value)
}

const handleBlur = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value

  if (props.mode === 'barcode') return // No formatear barcodes al salir

  const num = Number(value)
  if (isNaN(num)) {
    emit('update:modelValue', '0')
  } else {
    // Aquí sí formateamos para limpiar cosas como "00123" en modo precio
    const finalValue = props.mode === 'int' ? Math.trunc(num) : num
    emit('update:modelValue', finalValue.toString())
  }
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
input[type='number'] {
  -moz-appearance: textfield;
  appearance: textfield;
}
</style>
