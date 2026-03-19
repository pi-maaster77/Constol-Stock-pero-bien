<!-- frontend/src/views/DiscountsView.vue -->

<template>
	<DiscountTable @add="handleAdd" @edit="handleAdd"/>
	<DiscountMenu ref="modalRef" :move-detail="discountDetail"/>
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

function handleEdit(selectedIndexes: number[]) {
  const firstIndex = selectedIndexes[0]
  if (firstIndex === undefined) return
  discountDetail.value = discountStore.discounts[firstIndex]
  modalRef.value?.openModal()
}

</script>