<!-- frontend/src/App.vue -->

<script setup lang="ts">

import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import IncrementDecrement from '@/components/domain/IncrementDecrement.vue';
import TableProducts from './components/domain/TableProducts.vue';

import { useProductsStore } from '@/stores/product'
const productStore = useProductsStore()
productStore.load()
</script>

<template>
  <IncrementDecrement :min="0" :max="100"/>
  <TableProducts />
</template>