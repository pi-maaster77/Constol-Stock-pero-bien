<!-- frontend/src/components/ui/DumbMove.vue -->

<script setup lang="ts">
import type { Move } from '@/types/move'
import BootstapAccordeon from './BootstapAccordeon.vue';

const props = defineProps<{ move: Move; parentId?: string }>()

const moveStyles: Record<string, { class: string; label: string; icon: string }> = {
  in: { class: 'bg-success-subtle text-success border-success', label: 'ENTRADA', icon: 'bi-arrow-down-left-circle' },
  out: { class: 'bg-danger-subtle text-danger border-danger', label: 'SALIDA', icon: 'bi-arrow-up-right-circle' },
  adjust: { class: 'bg-warning-subtle text-warning-emphasis border-warning', label: 'AJUSTE', icon: 'bi-sliders' },
}

const currentStyle = moveStyles[props.move.type] || { class: 'bg-light', label: props.move.type, icon: 'bi-info-circle' }
const formatCurrency = (val: number) => new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(val)
</script>

<template>
  <BootstapAccordeon :id="move.id" :parent-container-id="parentId">
    
    <template #header>
      <div class="d-flex justify-content-between align-items-center w-100 me-3">
        <div>
          <span :class="['badge border me-2', currentStyle.class]">
            <i :class="['bi me-1', currentStyle.icon]"></i> {{ currentStyle.label }}
          </span>
          <span class="text-secondary small fw-normal">{{ move.date }}</span>
        </div>
        <span class="fw-bold">ID #{{ move.id }}</span>
      </div>
    </template>

    <template #content>
      <div class="table-responsive">
        <table class="table table-sm table-hover mb-0 align-middle">
          <tbody>
            <tr v-for="item in move.details" :key="item.id_product">
              <td class="ps-3">
                <div class="fw-bold">{{ item.product_name }}</div>
                <div class="font-monospace text-muted x-small">SKU: {{ item.bc_product }}</div>
              </td>
              <td class="text-center fw-bold">{{ item.ammount }}</td>
              <td class="text-end text-muted small">{{ formatCurrency(item.unit_price) }}</td>
              <td class="text-end pe-3 fw-bold">{{ formatCurrency(item.total_price) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

  </BootstapAccordeon>
</template>