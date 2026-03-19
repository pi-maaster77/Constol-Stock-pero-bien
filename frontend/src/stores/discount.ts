// frontend/src/stores/discount.ts

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { createDiscount, deleteDiscount, getDiscount, updateDiscount } from '@/api/discount_bulk'
import { useNotificationsStore } from './notifications'
import type { Discount, DiscountUpdate } from '@/types/discounts'

export const useDiscountsStore = defineStore('discounts', () => {
  const discounts = ref<Discount[]>([])
  const discountsCount = computed(() => discounts.value.length)

  function isAxiosError(error: unknown): error is {
    response?: { data?: { message?: string } }
    message?: string
  } {
    return typeof error === 'object' && error !== null
  }

  async function optimistic(fn: Function, request: Function) {
    const backup = [...discounts.value]
    const notify = useNotificationsStore()

    try {
      fn()
      await request()
    } catch (e: unknown) {
      discounts.value.splice(0, discounts.value.length, ...backup)
      console.error(e)

      let msg = 'Ocurrió un error inesperado'

      if (isAxiosError(e)) {
        msg = e.response?.data?.message || e.message || msg
      }
      notify.push('error', msg)
    }
  }

  function load() {
    optimistic(
      () => {},
      async () => {
        const res = await getDiscount()

        const mapped: Discount[] = res

        discounts.value.splice(0, discounts.value.length, ...mapped)
      },
    )
  }

  function getDiscountByID(id: number): Discount | undefined {
    return discounts.value.find((d) => d.id === id) as Discount | undefined
  }

  function create(value: Omit<Discount, 'id'>) {
    optimistic(
      () => {
        const tempID = Math.max(0, ...discounts.value.map((p) => p.id)) + 1
        discounts.value.push({ id: tempID, ...value })
      },
      async () => {
        const res = await createDiscount({
          discount: value.discount,
          id_product: value.id_product,
          min_ammount: value.min_ammount,
        })
        load()
      },
    )
  }

  function updateByID(id: number, value: Omit<Discount, 'id'>) {
    optimistic(
      () => {
        const tempID = Math.max(0, ...discounts.value.map((p) => p.id)) + 1
        discounts.value.push({ id: tempID, ...value })
      },
      async () => {
        const res = await updateDiscount(id, {
          discount: value.discount,
          min_ammount: value.min_ammount,
        })
        load()
      },
    )
  }

  function deleteByID(id: number) {
    optimistic(
      () => {
        const index = discounts.value.findIndex((p) => p.id === id)
        if (index !== -1) {
          discounts.value.splice(index, 1)
        }
      },
      async () => {
        await deleteDiscount(id)
        load()
      },
    )
  }

  return { discounts, discountsCount, load, getDiscountByID, updateByID, deleteByID, create }
})
