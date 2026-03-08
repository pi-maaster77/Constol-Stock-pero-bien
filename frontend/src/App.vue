<!-- frontend/src/App.vue -->

<script setup lang="ts">

import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import BuySellProduct from '@/components/domain/BuySellProduct.vue';
import TableProducts from './components/domain/TableProducts.vue';

import { useProductsStore } from '@/stores/product'
import CreateEditProduct from './components/domain/CreateEditProduct.vue';
const productStore = useProductsStore()
productStore.load()
</script>

<template>
  <CreateEditProduct :product="null"/>
  <TableProducts />
</template>