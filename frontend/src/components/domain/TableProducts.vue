<!-- frontend/src/components/domain/TableProducts.vue -->

<template>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Precio</th>
                <th>Stock</th>
            </tr>
        </thead>
        <tbody>
            <DumbProduct v-for="product in products" :key="product.id" :product="{price: product.public_price, stock: product.id, name: product.name}" />
        </tbody>
    </table>
</template>

<script setup lang="ts">    

import { useProductsStore } from '@/stores/product'
import DumbProduct from '@/components/ui/DumbProduct.vue'
const productStore = useProductsStore()
const { products } = productStore


</script>