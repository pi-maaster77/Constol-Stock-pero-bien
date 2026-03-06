<!-- frontend/src/components/ui/DumbProduct.vue -->

<template>
    <tr>
        <td>{{ product.bc }}</td>
        <td>{{ product.name }}</td>
        <td>{{ product.public_price }}</td>
        <td>{{ product.ammount }}</td>
        <td class="btn-group" role="group">
            <ButtonEdit @click="handleEdit" />
            <ButtonDelete @click="handleDelete" />
        </td>
    </tr>
</template>

<script setup lang="ts">
import type { Product } from '@/types/product'
import ButtonDelete from './Buttons/ButtonDelete.vue';
import ButtonEdit from './Buttons/ButtonEdit.vue';
const props = defineProps<{
    product: Product
}>()

const emit = defineEmits<{
    (e: 'edit', product: Product): void
    (e: 'delete', product: Product): void
}>()

function handleEdit() {
    emit('edit', props.product)
}
function handleDelete() {
    emit('delete', props.product)
}


</script>