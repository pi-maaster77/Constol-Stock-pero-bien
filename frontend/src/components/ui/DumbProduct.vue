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
    <td>{{ product.public_price }}</td>
    <td>{{ product.ammount }}</td>
		<td v-if="expireDate">{{ expireDate }}</td>
  </tr>
</template>

<script setup lang="ts">
import type { ISODateString } from '@/types/ISODatingFormat';
import type { Product } from '@/types/product'
const props = defineProps<{
  product: Product
  productIndex?: number
  checked?: boolean
	expireDate?: ISODateString
}>()

const emit = defineEmits<{
  (e: 'edit', product: Product): void
  (e: 'delete', product: Product): void
  (e: 'toggle', id: number): void
}>()

function toggle() {
  console.log('toggled', props.product.id)
  emit('toggle', props.product.id)
}
</script>
