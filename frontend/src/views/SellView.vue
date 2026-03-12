<!-- frontend/src/views/SellView.vue -->

<template>
  <TableSell @add="handleAdd" @edit="handleEdit"/>
  <BuySellAdjustProduct ref="modalRef" mode="sell" :move-detail="moveDetail" />
</template>

<script setup lang="ts">
import BuySellAdjustProduct from '@/components/domain/BuySellAdjustProduct.vue'
import TableSell from '@/components/domain/TableSell.vue'
import { useSellStore } from '@/stores/sell'
import { ref } from 'vue'

const sellStore = useSellStore()
const modalRef = ref()
const moveDetail = ref<any>(null)

function handleAdd() {
  moveDetail.value = null
  modalRef.value?.openModal()
}

function handleEdit(selectedIndexes: number[]) {
  const firstIndex = selectedIndexes[0]
  if (firstIndex === undefined) return
  moveDetail.value = sellStore.products[firstIndex]
  modalRef.value?.openModal()
}
</script>
