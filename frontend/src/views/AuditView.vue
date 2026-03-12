<!-- frontend/src/views/AuditView.vue -->

<template>
  <TableAudit @add="handleAdd" @edit="handleEdit" @upload="handleUpload" />
  <BuySellAdjustProduct ref="modalAdjustRef" mode="adjust" :move-detail="moveDetail"/>
  <UploadAudit ref="modalConfirmRef" />
</template>

<script setup lang="ts">
import BuySellAdjustProduct from '@/components/domain/BuySellAdjustProduct.vue'
import TableAudit from '@/components/domain/TableAudit.vue'
import UploadAudit from '@/components/domain/UploadAudit.vue'
import { useAuditStore } from '@/stores/audit'
import { ref } from 'vue'

const auditStore = useAuditStore()
const modalAdjustRef = ref()
const modalConfirmRef = ref()
const moveDetail = ref<any>(null)

function handleAdd() {
  moveDetail.value = null
  modalAdjustRef.value?.openModal()
}

function handleEdit(selectedIndexes: number[]){
  const firstIndex = selectedIndexes[0]
  if (firstIndex === undefined) return
  moveDetail.value = auditStore.products[firstIndex]
  modalAdjustRef.value?.openModal()
}

function handleUpload() {
  modalConfirmRef.value?.openModal()
}
</script>
