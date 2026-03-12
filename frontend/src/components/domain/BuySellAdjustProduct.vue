<!-- frontend/src/components/domain/BuySellAdjustProduct.vue -->

<script setup lang="ts">
import { getProductByBC } from '@/api/product'
import type { Product } from '@/types/product'
import { ref, watch, computed, onMounted } from 'vue'
import NumberInput from '@/components/ui/Inputs/NumberInput.vue'
import NumberInputWithButtons from '@/components/ui/Inputs/NumberInputWithButtons.vue'
import TextArea from '@/components/ui/Inputs/TextArea.vue'
import TextInput from '@/components/ui/Inputs/TextInput.vue'
import { Modal } from 'bootstrap'
import DateInput from '../ui/Inputs/DateInput.vue'
import { useDiscountsStore } from '@/stores/discount'
import type { NewMoveDetail } from '@/types/move'
import { useAuditStore } from '@/stores/audit'
import { ISODateString } from '@/types/ISODatingFormat'
import { useBuyStore } from '@/stores/buy'
import { useSellStore } from '@/stores/sell'


const discountStore = useDiscountsStore()

const props = defineProps<{
  mode: 'buy' | 'sell' | 'adjust'
  moveDetail?: NewMoveDetail | null
}>()

const store = props.mode ==='adjust' ? useAuditStore(): 
							props.mode === 'buy' ? useBuyStore(): 
							props.mode === 'sell' ? useSellStore():
							useAuditStore()

const barcode = ref<string | null>(props.moveDetail?.product.bc ?? null)
const product = ref<Product | null>(props.moveDetail?.product ?? null)
const isLoading = ref(false)
const productNotFound = ref(false)

// Producto a agregar a detalle
const ammount = ref(props.moveDetail?.ammount ?? 0)
const ammountBridge = computed({
  get: () => ammount.value.toString(),
  set: (val) => {
    ammount.value = parseFloat(val) || 0
  },
})
const price = ref(props.moveDetail?.cost_price ?? 0)
const priceBridge = computed({
  get: () => price.value.toString(),
  set: (val) => {
    price.value = parseFloat(val) || 0
  },
})

const finalPrice = computed(() => {
  const currentAmmount = ammount.value

  // 1. Si no hay producto, el precio es 0
  if (!product?.value) return 0

  // 2. Lógica para VENTA (Donde aplican los descuentos)
  if (props.mode === 'sell') {
    const basePrice = product.value.public_price || 0

    const applicableDiscount = discountStore.discounts
      .filter((d) => d.id_product === product.value?.id && currentAmmount >= d.min_ammount)
      .sort((a, b) => b.min_ammount - a.min_ammount)[0] // Tomamos el de mayor rango alcanzado

    if (applicableDiscount) {
      // Aplicamos el precio especial del descuento
      return parseFloat(
        (product.value.public_price * (1 - applicableDiscount.discount) * currentAmmount).toFixed(
          2,
        ),
      )
    }

    // Si no hay descuento, precio normal
    return basePrice * currentAmmount
  }

  // 3. Lógica para COMPRA o AJUSTE (Se usa el precio del input manual)
  return price.value * currentAmmount
})
const expirationDate = ref<string>(props.moveDetail?.expires_at?.toISOString() ?? '') // Formato YYYY-MM-DD

// Watcher para buscar automáticamente cuando el barcode cambie
watch(barcode, async (newVal) => {
  if (!newVal) {
    product.value = null
    productNotFound.value = false
    return
  }

  isLoading.value = true
  productNotFound.value = false

  try {
    const data = await getProductByBC(newVal.toString())
    if (data) {
      product.value = data
      productNotFound.value = false
    } else {
      throw new Error()
    }
  } catch (error) {
    product.value = null
    productNotFound.value = true
  } finally {
    isLoading.value = false
  }
})

// Nombre dinámico para mostrar en el input deshabilitado
const displayName = computed(() => {
  if (isLoading.value) return 'Buscando producto...'
  if (productNotFound.value) return 'Producto no encontrado'
  return product.value?.name || ''
})

let modal: Modal

onMounted(() => {
  const el = document.getElementById('BuySellProductModal')
  modal = new Modal(el!)
  discountStore.load()
})

function openModal() {
  modal.show()
}

function closeModal() {
  modal.hide()
}

function increment() {
  ammount.value++
}
function decrement() {
  if (props.mode === 'adjust') {
    ammount.value--
  } else if (ammount.value > 0) {
    ammount.value--
  }
}

function handleDetail() {
  const expiresAtDate = expirationDate.value ? new ISODateString(expirationDate.value) : null
  if (product.value !== undefined && product.value !== null) {
    store.create({
      ammount: ammount.value,
      cost_price: price.value,
      expires_at: expiresAtDate,
      id_product: product.value.id,
      product: product.value,
      received_at: new ISODateString(new Date()),
    })
  }
  closeModal()
}

function handleSave() {
  const expiresAtDate = expirationDate.value ? new ISODateString(expirationDate.value) : null
  if (product.value !== undefined && product.value !== null && props.moveDetail) {
    // Buscar el índice del producto en el store
    const editIndex = store.products.findIndex(
      (p) => p.id_product === product.value!.id && p.received_at.toISOString() === props.moveDetail!.received_at.toISOString()
    )
    
    if (editIndex !== -1) {
      store.updateByID(editIndex, {
        ammount: ammount.value,
        cost_price: price.value,
        expires_at: expiresAtDate,
        id_product: product.value.id,
        product: product.value,
        received_at: props.moveDetail!.received_at,
      })
    }
  }
  closeModal()
}

defineExpose({
  openModal,
})
</script>

<template>
  <div
    class="modal fade"
    id="BuySellProductModal"
    tabindex="-1"
    aria-labelledby="BuySellProductModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">
            <span v-if="props.mode === 'buy'">Comprar</span
            ><span v-if="props.mode === 'sell'">Vender</span
            ><span v-if="props.mode === 'adjust'">Ajustar</span>
          </h1>

          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="closeModal"
          ></button>
        </div>

        <div class="modal-body">
          <NumberInput
            mode="barcode"
            v-model="barcode"
            :class="{
              'is-invalid': productNotFound,
              'is-loading': isLoading,
              'mb-3': true,
            }"
          >
            <template #label><label class="form-label">Código de barras</label></template>
          </NumberInput>

          <div
            v-if="isLoading"
            class="spinner-border spinner-border-sm position-absolute end-0 top-50 mb-3 me-3"
            role="status"
          >
            <span class="visually-hidden">Cargando...</span>
          </div>

          <div v-if="productNotFound" class="invalid-feedback d-block mb-3">
            El código ingresado no coincide con ningún producto.
          </div>
          <TextInput
            :model-value="displayName"
            :disabled="true"
            :class="{
              'text-danger': productNotFound,
              'mb-3': true,
            }"
          >
            <template #label><label class="form-label">Nombre</label></template>
          </TextInput>

          <NumberInputWithButtons
            v-model="ammountBridge"
            :class="{ 'mb-3': true }"
            @increment="increment"
            @decrement="decrement"
          >
            <template #label><label class="form-label">Cantidad</label></template>
          </NumberInputWithButtons>
          <div v-if="mode === 'buy' || mode === 'adjust' && ammount > 0">
            <NumberInput v-model="priceBridge" :class="{ 'mb-3': true }" mode="float">
              <template #label><label class="form-label">Precio</label></template>
            </NumberInput>

            <DateInput v-model="expirationDate" v-if="product?.expires">
              <template #label><label class="form-label">Fecha de vencimiento</label></template>
            </DateInput>
          </div>
          <div v-if="mode === 'sell'">
            <p class="text-muted small">Precio unitario: {{ product?.public_price || 0 }}</p>
            <p class="text-muted small">
              Precio subtotal: {{ (product?.public_price || 0) * ammount }}
            </p>
            <p class="text-muted small">Precio total: {{ finalPrice }}</p>
          </div>
          <div class="modal-footer">
						<button type="button" class="btn btn-primary" @click="handleSave" v-if="props.moveDetail">Guardar</button>
            <button type="button" class="btn btn-primary" @click="handleDetail" v-else>Crear</button>
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
