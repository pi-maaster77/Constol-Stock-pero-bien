<!-- frontend/src/views/BuyView.vue -->

<template>
  <TableBuy @add="handleAdd" @edit="handleEdit"/>
  <BuySellAdjustProduct ref="modalRef" mode="buy" :move-detail="moveDetail" />
</template>

<script setup lang="ts">
import BuySellAdjustProduct from '@/components/domain/BuySellAdjustProduct.vue'
import TableBuy from '@/components/domain/TableBuy.vue'
import { useAuditStore } from '@/stores/audit'
import { ref } from 'vue'

const auditStore = useAuditStore()
const modalRef = ref()
const moveDetail = ref<any>(null)

function handleAdd() {
  moveDetail.value = null
  modalRef.value?.openModal()
}

function handleEdit(selectedIndexes: number[]) {
  const firstIndex = selectedIndexes[0]
  if (firstIndex === undefined) return
  moveDetail.value = auditStore.products[firstIndex]
  modalRef.value?.openModal()
}
</script>
