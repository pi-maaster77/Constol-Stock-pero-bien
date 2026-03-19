<!-- frontend/src/App.vue -->

<script setup lang="ts">
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import ProductsView from './views/ProductsView.vue'

import { computed, markRaw, ref } from 'vue'
import TableMoves from './components/domain/TableMoves.vue'
import MovesView from './views/MovesView.vue'
import BuySellAdjustProduct from './components/domain/BuySellAdjustProduct.vue'
import TableAudit from './components/domain/TableAudit.vue'
import AuditView from './views/AuditView.vue'
import BuyView from './views/BuyView.vue'
import SellView from './views/SellView.vue'
import DiscountsView from './views/DiscountsView.vue'
const activeTab = ref('products')

// Usamos markRaw para que Vue no intente hacer reactivos los objetos de los componentes (mejora rendimiento)
const tabs: Record<string, { label: string, icon: string, component: any }> = {
  products: { label: 'Productos', icon: 'bi-table', component: markRaw(ProductsView) },
  moves: { label: 'Entradas/Salidas', icon: 'bi-arrow-left-right', component: markRaw(MovesView) },
  buy: { label: 'Comprar', icon: 'bi-bag', component: markRaw(BuyView) },
  sell: { label: 'Vender', icon: 'bi-receipt-cutoff', component: markRaw(SellView) },
  audit: { label: 'Auditar', icon: 'bi-archive', component: markRaw(AuditView) },
  discount: { label: 'Descuentos', icon: 'bi-percent', component: markRaw(DiscountsView) },
  tests: { label: 'Pruebas', icon: 'bi-flask', component: null } // O un componente de pruebas
}

const currentComponent = computed(() => tabs[activeTab.value]?.component)
</script>

<template>
  <div class="container-fluid mt-3">
    <ul class="nav nav-tabs custom-notebook" role="tablist">
      <li v-for="(tab, key) in tabs" :key="key" class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === key }"
          @click="activeTab = key"
          type="button"
        >
          <i :class="tab.icon" class="me-2"></i>{{ tab.label }}
        </button>
      </li>
    </ul>

    <div class="tab-content border-start border-end border-bottom p-4 shadow-sm">
      <component :is="currentComponent" v-if="currentComponent" />
      
      <div v-else>
        <p class="text-muted">Sección {{ activeTab }} en desarrollo...</p>
      </div>
    </div>
  </div>
</template>