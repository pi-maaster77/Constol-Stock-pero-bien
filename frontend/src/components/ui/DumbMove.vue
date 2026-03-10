<!-- frontend/src/components/ui/DumbMove.vue -->

<script setup lang="ts">
import type { Move } from '@/types/move'

const props = defineProps<{
    disabled: boolean
    move: Move
}>()

// Lógica de UI para los estados
const moveStyles: Record<string, { class: string; label: string; icon: string }> = {
  in: { class: 'bg-success-subtle text-success border-success', label: 'ENTRADA', icon: 'bi-arrow-down-left-circle' },
  out: { class: 'bg-danger-subtle text-danger border-danger', label: 'SALIDA', icon: 'bi-arrow-up-right-circle' },
  adjustment: { class: 'bg-warning-subtle text-warning-emphasis border-warning', label: 'AJUSTE', icon: 'bi-sliders' }
}

const currentStyle = moveStyles[props.move.type] || { class: 'bg-light', label: props.move.type, icon: 'bi-info-circle' }

const formatCurrency = (val: number) => new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(val)
</script>

<template>
  <div class="accordion-item mb-2 border rounded shadow-sm">
    <h2 class="accordion-header">
      <button 
        class="accordion-button collapsed py-2" 
        type="button" 
        data-bs-toggle="collapse" 
        :data-bs-target="`#move-${move.id}`"
      >
        <div class="d-flex justify-content-between align-items-center w-100 me-3">
          <div>
            <span :class="['badge border me-2', currentStyle.class]">
              <i :class="['bi me-1', currentStyle.icon]"></i> {{ currentStyle.label }}
            </span>
            <span class="text-secondary small fw-normal">{{ move.date}}</span>
          </div>
          <span class="fw-bold">ID #{{ move.id }}</span>
        </div>
      </button>
    </h2>

    <div :id="`move-${move.id}`" class="accordion-collapse collapse">
      <div class="accordion-body p-0">
        <div class="table-responsive">
          <table class="table table-sm table-hover mb-0 align-middle">
            <thead class="table text-uppercase" style="font-size: 0.7rem;">
              <tr>
                <th class="ps-3">Producto / BC</th>
                <th class="text-center">Cant.</th>
                <th class="text-end">P. Unit</th>
                <th class="text-end pe-3">Subtotal</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in move.details" :key="item.id_product">
                <td class="ps-3">
                  <div class="fw-bold text">{{ item.product_name }}</div>
                  <div class="font-monospace text-muted x-small">SKU: {{ item.bc_product }}</div>
                </td>
                <td class="text-center fw-bold">{{ item.ammount }}</td>
                <td class="text-end text-muted small">{{ formatCurrency(item.unit_price) }}</td>
                <td class="text-end pe-3 fw-bold">{{ formatCurrency(item.total_price) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.x-small { font-size: 0.7rem; }
.accordion-button:focus { box-shadow: none; }
.accordion-button:not(.collapsed) {
  background-color: transparent;
  color: inherit;
}
</style>