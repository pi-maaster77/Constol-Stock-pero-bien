<!-- frontend/src/components/domain/TableMoves.vue -->

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import DumbMove from '@/components/ui/DumbMove.vue'
import type { Move } from '@/types/move'
import { ISODateString } from '@/types/ISODatingFormat'
import { useMovesStore } from '@/stores/moves'

const movesStore = useMovesStore()

onMounted(async () => {
    try {
        movesStore.load()
    } catch (error) {
        console.error("Error al cargar movimientos:", error)
    }  
})



const isLoading = ref(false)
</script>

<template>
  <div class="container mt-4">
    <h3 class="mb-3">Historial de Movimientos</h3>

    <div class="accordion" id="movesAccordion">
      
      <DumbMove 
        v-for="item in movesStore.moves" 
        :key="item.id"
        :move="item as Move"
        :disabled="isLoading"
      />

      <div v-if="movesStore.moves.length === 0" class="text-center p-5 border rounded bg">
        <p class="text-muted">No hay movimientos registrados.</p>
      </div>

    </div>
  </div>
</template>