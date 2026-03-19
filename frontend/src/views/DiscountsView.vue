<!-- frontend/src/views/DiscountsView.vue -->

<template>
  <DiscountTable @add="handleAdd" @edit="handleEdit"/>
  <DiscountMenu ref="modalRef" :discount="discountDetail"/>
</template>
<script setup lang="ts">
import DiscountMenu from '@/components/domain/DiscountMenu.vue';
import DiscountTable from '@/components/domain/DiscountTable.vue';
import { useDiscountsStore } from '@/stores/discount';
import { ref } from 'vue';

const discountStore = useDiscountsStore()
const modalRef = ref()
const discountDetail = ref<any>(null)

function handleAdd() {
  discountDetail.value = null
  modalRef.value?.openModal()
}

function handleEdit(selectedIds: number[]) {
  const firstId = selectedIds[0]
  if (firstId === undefined) return
  
  // Buscamos el objeto real por su ID único
  const discountToEdit = discountStore.discounts.find(d => d.id === firstId)
  
  if (discountToEdit) {
    discountDetail.value = discountToEdit
    modalRef.value?.openModal()
  }
}

</script>