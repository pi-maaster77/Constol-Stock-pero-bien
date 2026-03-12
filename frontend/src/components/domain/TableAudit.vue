<!-- frontend/src/components/domain/TableAudit.vue -->

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAuditStore } from '@/stores/audit'
import DumbProduct from '@/components/ui/DumbProduct.vue'
import ButtonAccept from '../ui/Buttons/ButtonAccept.vue'
import ButtonAdd from '../ui/Buttons/ButtonAdd.vue'
import ButtonEdit from '../ui/Buttons/ButtonEdit.vue'
import ButtonDelete from '../ui/Buttons/ButtonDelete.vue'
// ... otros imports

const productAtributes = ['Código de barras', 'Nombre', 'Precio', 'Cantidad']

const auditStore = useAuditStore()
const selectedIndexes = ref<number[]>([]) // Ahora guardamos la posición en el array

const allSelected = computed(
  () => auditStore.productCount > 0 && selectedIndexes.value.length === auditStore.productCount,
)

const disabled = computed(() => selectedIndexes.value.length === 0)

// Para editar, pasamos los objetos reales basados en los índices seleccionados
const selectedProducts = computed(() =>
  selectedIndexes.value.map((index) => auditStore.products[index]),
)

function toggleAll() {
  if (allSelected.value) {
    selectedIndexes.value = []
  } else {
    // Llenamos con [0, 1, 2, ...] hasta el total de productos
    selectedIndexes.value = auditStore.products.map((_, index) => index)
  }
}

function toggleProduct(index: number) {
  const idx = selectedIndexes.value.indexOf(index)
  if (idx > -1) {
    selectedIndexes.value.splice(idx, 1)
  } else {
    selectedIndexes.value.push(index)
  }
}

const emit = defineEmits<{
  (e: 'add'): void
  (e: 'edit', selectedIds: number[]): void
  (e: 'upload'): void
}>()

function handleUpload() {
  emit('upload')
}

function handleAdd() {
  emit('add')
}

function handleEdit() {
  emit('edit', selectedIndexes.value)
}

function handleDelete() {
  // TRUCO CLAVE: Ordenar índices de mayor a menor
  // Si borras el índice 10 primero, el índice 2 sigue siendo el mismo.
  const sortedIndexes = [...selectedIndexes.value].sort((a, b) => b - a)

  sortedIndexes.forEach((index) => {
    auditStore.deleteByID(index)
  })

  selectedIndexes.value = [] // Limpiar selección
}
</script>

<template>
  <div class="container mt-4">
    <h3 class="mb-3">Auditar Productos</h3>
    <div class="mb-3 btn-group" role="group">
      <ButtonAdd @click="handleAdd" />
      <ButtonEdit @click="handleEdit" :disabled="disabled" />
      <ButtonDelete @click="handleDelete" :disabled="disabled" />
      <ButtonAccept @click="handleUpload" :disabled="auditStore.productCount <= 0" />
    </div>
    <table class="table">
      <thead>
        <tr>
          <th>
            <input
              type="checkbox"
              name="select-all"
              id="select-all"
              class="form-check-input"
              :checked="allSelected"
              @change="toggleAll"
            />
          </th>
          <th v-for="header in productAtributes" :key="header">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <DumbProduct
          v-for="(product, index) in auditStore.products"
          :key="index"
          :product="product.product"
          :adjust-ammount="product.ammount"
          :checked="selectedIndexes.includes(index)"
          @toggle="toggleProduct(index)"
        />
      </tbody>
    </table>
  </div>
</template>
