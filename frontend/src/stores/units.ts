// frontend/src/stores/units.ts

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getUnit } from '@/api/unit'

import type { Unit, UnitCreate, UnitUpdate } from '@/types/unit'
import { useNotificationsStore } from './notifications'
import { ISODateString } from '@/types/ISODatingFormat'

export const useUnitsStore = defineStore('units', () => {
  const units = ref<Unit[]>([])
  const unitCount = computed(() => units.value.length)

  function isAxiosError(error: unknown): error is {
    response?: { data?: { message?: string } }
    message?: string
  } {
    return typeof error === 'object' && error !== null
  }

  async function optimistic(fn: Function, request: Function) {
    const backup = [...units.value]
    const notify = useNotificationsStore()

    try {
      fn()
      await request()
    } catch (e: unknown) {
      units.value.splice(0, units.value.length, ...backup)
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
        const res = await getUnit()

        const mapped: Unit[] = res as Unit[]

        units.value.splice(0, units.value.length, ...mapped)
      },
    )
  }

  function getUnitByID(id: number): Unit | undefined {
    return units.value.find((u) => u.id === id) as Unit | undefined
  }

  function set(value: Unit[]) {
    units.value.splice(0, units.value.length, ...value)
  }

  return { units, unitCount, load, getUnitByID, set }
})
