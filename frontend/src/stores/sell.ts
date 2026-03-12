// frontend/src/stores/sell.ts

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import type { NewMoveDetail } from '@/types/move'

export const useSellStore = defineStore('sell', () => {
  const products = ref<NewMoveDetail[]>([])
  const productCount = computed(() => products.value.length)

  function create(moveDetail: NewMoveDetail) {
    products.value.push(moveDetail)
  }

  function updateByID(id: number, moveDetail: NewMoveDetail) {
    products.value[id] = moveDetail
  }

  function deleteByID(id: number) {
    if (id >= 0 && id < products.value.length) {
      products.value.splice(id, 1)
    }
  }
  return { products, productCount, create, updateByID, deleteByID }
})
