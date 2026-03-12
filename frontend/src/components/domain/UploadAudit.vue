<!-- frontend/src/components/domain/UploadAudit.vue -->

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Modal } from 'bootstrap'
import { useAuditStore } from '@/stores/audit'
import TextArea from '../ui/Inputs/TextArea.vue'
import { movesAdjust } from '@/api/moves'
import { ISODateString } from '@/types/ISODatingFormat'

const auditStore = useAuditStore()

const reason = ref('')

let modal: Modal

onMounted(() => {
  // usar el ID correcto del modal de confirmación
  const el = document.getElementById('BuyConfirmModal')
  modal = new Modal(el!)
})

function openModal() {
  modal.show()
}

function closeModal() {
  modal.hide()
}

function handleDetail() {
  movesAdjust(
    {
      date: (new ISODateString(new Date()).toISOString()) as unknown as ISODateString, 
      details: auditStore.products.map((p) => ({
        id_product: p.id_product,
        received_at: typeof p.received_at === 'string' ? p.received_at : p.received_at.toISOString(),
        expires_at: p.expires_at ? (typeof p.expires_at === 'string' ? p.expires_at : p.expires_at.toISOString()) : null,
        ammount: p.ammount,
        cost_price: p.cost_price,
      })),
      reason: reason.value,
    },
  ).then(() => {
    auditStore.products = []
    closeModal()
  }).catch((error) => {
    console.error('Error uploading audit:', error)
  })
}

defineExpose({
  openModal,
})
</script>

<template>
  <div
    class="modal fade"
    id="BuyConfirmModal"
    tabindex="-1"
    aria-labelledby="BuyConfirmModal"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="BuyConfirmModalLabel">Confirmar Ajuste</h1>

          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <TextArea v-model="reason">
            <template #label><label class="form-label">Motivo</label></template>
          </TextArea>

          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="handleDetail">Crear</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Estilo para simular carga si tu componente NumberInput no lo tiene */
.is-loading {
  opacity: 0.7;
  pointer-events: none;
}
</style>
