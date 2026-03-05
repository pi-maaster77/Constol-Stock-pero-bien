<!-- frontend/src/components/ui/DumbProduct.vue -->

<template>
    <tr>
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.stock }}</td>
    </tr>
</template>

<script setup lang="ts">
defineProps<{
    product: {
        name: string
        price: number
        stock: number
    }
}>()

</script>