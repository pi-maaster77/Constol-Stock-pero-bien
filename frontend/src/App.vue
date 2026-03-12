<!-- frontend/src/App.vue -->

<script setup lang="ts">
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import ProductsView from './views/ProductsView.vue'

import { ref } from 'vue'
import TableMoves from './components/domain/TableMoves.vue'
import MovesView from './views/MovesView.vue'
import BuySellAdjustProduct from './components/domain/BuySellAdjustProduct.vue'
import TableAudit from './components/domain/TableAudit.vue'
import AuditView from './views/AuditView.vue'
import BuyView from './views/BuyView.vue'
const activeTab = ref('Productos')
</script>

<template>
  <div class="container-fluid mt-3">
    <ul class="nav nav-tabs custom-notebook" role="tablist">
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'products' }"
          @click="activeTab = 'products'"
          type="button"
        >
          <i class="bi bi-table me-2"></i>Productos
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'moves' }"
          @click="activeTab = 'moves'"
          type="button"
        >
          <i class="bi bi-arrow-left-right me-2"></i>Entradas/Salidas
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'buy' }"
          @click="activeTab = 'buy'"
          type="button"
        >
          <i class="bi bi-bag me-2"></i>Comprar
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'sell' }"
          @click="activeTab = 'sell'"
          type="button"
        >
          <i class="bi bi-basket me-2"></i>Vender
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'audit' }"
          @click="activeTab = 'audit'"
          type="button"
        >
          <i class="bi bi-archive me-2"></i>Auditar
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: activeTab === 'tests' }"
          @click="activeTab = 'tests'"
          type="button"
        >
          <i class="bi bi-flask me-2"></i>Pruebas
        </button>
      </li>
    </ul>

    <div class="tab-content border-start border-end border-bottom p-4 shadow-sm">
      <div v-if="activeTab === 'products'" class="tab-pane fade show active">
        <ProductsView />
      </div>

      <div v-if="activeTab === 'moves'" class="tab-pane fade show active">
        <MovesView />
      </div>
      <div v-if="activeTab === 'buy'">
        <BuyView />
      </div>
      <div v-if="activeTab === 'sell'">
        <AuditView />
      </div>
      <div v-if="activeTab === 'audit'">
        <AuditView />
      </div>
      <div v-if="activeTab === 'pruebas'"></div>
		</div>
  </div>
</template>
