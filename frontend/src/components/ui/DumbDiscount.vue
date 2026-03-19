<!-- frontend/src/components/ui/DumbDiscount.vue -->

<template>
  <tr v-if="product">
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
    <td>{{ percent*100 }}%</td>
    <td>{{ ammount }}</td>
  </tr>
	<tr v-else>
		<td>-</td>
		<td>Producto invalido</td>
		<td>-</td>
		<td>-</td>
		<td>-</td>
	</tr>
</template>

<script setup lang="ts">
import type { Product } from '@/types/product'
const props = defineProps<{
  product: Product | undefined | null
	ammount: number
	percent: number
	id: number
  checked?: boolean
}>()

const emit = defineEmits<{
  (e: 'toggle', id: number): void
}>()

function toggle() {
	if(props.product?.id){
  	emit('toggle', props.product.id)
	}
}
</script>
