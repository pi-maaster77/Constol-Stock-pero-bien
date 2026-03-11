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
const tabActiva = ref('Productos')
</script>

<template>
  <div class="container-fluid mt-3">
    <ul class="nav nav-tabs custom-notebook" role="tablist">
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: tabActiva === 'Productos' }"
          @click="tabActiva = 'Productos'"
          type="button"
        >
          <i class="bi bi-table me-2"></i>Productos
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: tabActiva === 'tags' }"
          @click="tabActiva = 'tags'"
          type="button"
        >
          <i class="bi bi-arrow-left-right me-2"></i>Entradas/Salidas
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: tabActiva === 'pruebas' }"
          @click="tabActiva = 'pruebas'"
          type="button"
        >
          <i class="bi bi-flask me-2"></i>Pruebas
        </button>
      </li>
    </ul>

    <div class="tab-content border-start border-end border-bottom p-4 shadow-sm">
      <div v-if="tabActiva === 'Productos'" class="tab-pane fade show active">
        <ProductsView />
      </div>

      <div v-if="tabActiva === 'tags'" class="tab-pane fade show active">
        <MovesView />
      </div>
      <div v-if="tabActiva === 'pruebas'">
        <BuySellAdjustProduct :mode="'sell'" :min="0" :max="100" />
      </div>
    </div>
  </div>
</template>
