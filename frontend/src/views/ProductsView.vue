<!-- frontend/src/views/ProductsView.vue -->

<template>
  <CreateEditProduct ref="modalRef" :product="currentProduct" />
  <TableProducts @add="handleAdd" @edit="handleEdit" />
</template>

<script setup lang="ts">
import CreateEditProduct from '@/components/domain/CreateEditProduct.vue'
import TableProducts from '@/components/domain/TableProducts.vue'
import { ref } from 'vue'
import type { Product } from '@/types/product'

const modalRef = ref()
const currentProduct = ref<Product | null>(null)

function handleAdd() {
  console.log('add')
  currentProduct.value = null
  modalRef.value?.openModal()
}
function handleEdit(product: Product[]) {
  if (product.length === 0) {
    console.error('No product selected for editing')
    return
  }
  currentProduct.value = product[0] ?? null // solo se edita el primero, aunque se puedan seleccionar varios
  modalRef.value.openModal()
}
function handleDelete(value: Product[]) {
  console.log('delete', value)
}
</script>
