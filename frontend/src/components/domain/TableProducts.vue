<!-- frontend/src/components/domain/TableProducts.vue -->

<template>
    <table class="table">
        <thead>
            <tr>
                <th v-for="header in productAtributes" :key="header">{{ header }}</th>
            </tr>
        </thead>
        <tbody>
            <DumbProduct v-for="product in products" :key="product.id" :product="product" />
        </tbody>
    </table>
</template>

<script setup lang="ts">    

import { useProductsStore } from '@/stores/product'
import DumbProduct from '@/components/ui/DumbProduct.vue'
const productAtributes = ['Código de barras', 'Nombre', 'Precio', 'Cantidad', 'Acciones']
const productStore = useProductsStore()
const { products } = productStore

</script>