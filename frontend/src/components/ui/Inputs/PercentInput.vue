<!-- frontend/src/components/ui/Inputs/PercentInput.vue -->

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    modelValue: string | number | null
    mode?: 'int' | 'float'
  }>(),
  {
    mode: 'float', // Por defecto float para porcentajes con decimales
  },
)

const emit = defineEmits<{
  (e: 'update:modelValue', value: string | null): void
}>()

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value

  // 1. Reemplazamos coma por punto para consistencia interna
  value = value.replace(',', '.')

  // 2. Limpieza según el modo
  if (props.mode === 'int') {
    value = value.replace(/[^0-9]/g, '')
  } else {
    // Permitir solo números y un único punto
    value = value.replace(/[^0-9.]/g, '')
    const parts = value.split('.')
    if (parts.length > 2) value = parts[0] + '.' + parts.slice(1).join('')
  }

  // 3. Validar rango máximo 100 en tiempo real (opcional, pero recomendado)
  const num = parseFloat(value)
  if (num > 100) value = "100"

  target.value = value.replace('.', ',') // Mostramos coma al usuario mientras escribe
  emit('update:modelValue', value) // Emitimos con punto para el backend/logic
}

const handleBlur = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value.replace(',', '.')
  
  let num = parseFloat(value)

  if (isNaN(num) || num < 0) {
    num = 0
  } else if (num > 100) {
    num = 100
  }

  // Formatear el valor final
  const finalValue = props.mode === 'int' ? Math.trunc(num) : num
  
  // Actualizamos el input visualmente a formato local
  target.value = finalValue.toString().replace('.', ',')
  emit('update:modelValue', finalValue.toString())
}
</script>

<template>
  <div class="input-wrapper">
    <div class="input-label" v-if="$slots.label">
      <slot name="label"></slot>
    </div>
    <div class="input-group">
      <input
        type="text"
        :value="modelValue?.toString().replace('.', ',')"
        @input="handleInput"
        @blur="handleBlur"
        class="form-control"
        placeholder="0,00"
      />
      <span class="input-group-text">%</span>
    </div>
  </div>
</template>