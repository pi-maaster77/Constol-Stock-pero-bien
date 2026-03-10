<!-- frontend/src/components/domain/BuySellProduct.vue -->

<template>
  <NumberInput mode="barcode" v-model="barcode" />
  <TextInput v-model="productName" :disabled="false"></TextInput>

  <NumberInputWithButtons id="count" v-model="count" @decrement="decrement" @increment="increment">
    <label for="count">Cantidad</label>
  </NumberInputWithButtons>
  <div v-if="mode === 'sell'">
    <p>Precio Unitario: {{ product?.public_price || 0 }}</p>
    <p>Precio Total: {{ (product?.public_price || 0) * count }}</p>
    <p>Descuento: {{}}</p>
    <!-- se debe consultar con la db-->
  </div>
  <div v-else>
    <NumberInput mode="float" v-model="price" />
    <DateInput v-if="product?.expires" v-model="expireDate" />
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import NumberInputWithButtons from '../ui/Inputs/NumberInputWithButtons.vue'
import { useCounterStore } from '@/stores/counter'
import NumberInput from '../ui/Inputs/NumberInput.vue'
import TextInput from '../ui/TextInput.vue'
import DateInput from '../ui/Inputs/DateInput.vue'

import type { Product } from '@/types/product'
const counterStore = useCounterStore()
const barcode = ref(0)
const product = ref<Product | null>(null)
const price = ref(product.value?.price_cache || 0)
const productName = ref('')
const expireDate = ref('')
const mode = ref<'buy' | 'sell'>('sell')
const count = computed({
  get: () => counterStore.count,
  set: (newValue) => {
    // Aquí validamos los límites antes de guardar en el store
    if (newValue >= props.min && newValue <= props.max) {
      counterStore.count = newValue
      // Si tu store no permite asignación directa, usa:
      // counterStore.setCount(newValue)
    }
  },
})

const props = defineProps<{
  min: number
  max: number
  product: Product | null
  mode: 'buy' | 'sell'
}>()

function decrement() {
  if (counterStore.count <= props.min) return
  counterStore.decrement()
}

function increment() {
  if (counterStore.count >= props.max) return
  counterStore.increment()
}
</script>
