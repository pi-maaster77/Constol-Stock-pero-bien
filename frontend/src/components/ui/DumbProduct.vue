<!-- frontend/src/components/ui/DumbProduct.vue -->

<template>
  <tr>
    <td>
      <input
        type="checkbox"
        class="form-check-input"
        :value="product.id"
        :checked="checked"
        @change="toggle"
      />
    </td>
    <td>{{ product.bc }}</td>
    <td>{{ product.name }}</td>
    <td>{{ price !== undefined ? price : product.public_price }}</td>
    <td>{{ adjustAmmount !== undefined ? adjustAmmount : product.ammount }}</td>
    <td v-if="expireDate">{{ expireDate }}</td>
  </tr>
</template>

<script setup lang="ts">
import type { Product } from '@/types/product'
const props = defineProps<{
  product: Product
  productIndex?: number
  checked?: boolean
  adjustAmmount?: number
  expireDate?: string
	price?: number
}>()

const emit = defineEmits<{
  (e: 'toggle', id: number): void
}>()

function toggle() {
  emit('toggle', props.product.id)
}
</script>
