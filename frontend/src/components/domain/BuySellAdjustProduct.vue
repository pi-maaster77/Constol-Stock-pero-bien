<!-- frontend/src/components/domain/BuySellAdjustProduct.vue -->

<!-- frontend/src/components/domain/BuySellProduct.vue -->

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

const props = defineProps<{
  mode: 'buy' | 'sell' | 'adjust'
}>()

const barcode = ref<string | null>(null)
const product = ref<Product | null>(null)
const isLoading = ref(false)
const productNotFound = ref(false)

// Producto a agregar a detalle
const ammount = ref(0)
const ammountBridge = computed({
  get: () => ammount.value.toString(),
  set: (val) => {
    ammount.value = parseFloat(val) || 0
  },
})
const price = ref(0)
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
    
    // Buscamos si hay un descuento por volumen para este producto y esta cantidad
    // Nota: Buscamos el descuento que pide la mayor cantidad pero que sea <= a la actual
    const applicableDiscount = discountsStore.discounts
      .filter(d => d.product_id === product.value?.id && currentAmmount >= d.min_quantity)
      .sort((a, b) => b.min_quantity - a.min_quantity)[0] // Tomamos el de mayor rango alcanzado

    if (applicableDiscount) {
      // Aplicamos el precio especial del descuento
      return applicableDiscount.discount_price * currentAmmount
    }

    // Si no hay descuento, precio normal
    return basePrice * currentAmmount
  }

  // 3. Lógica para COMPRA o AJUSTE (Se usa el precio del input manual)
  return price.value * currentAmmount
})
const expirationDate = ref(new Date().toISOString().substr(0, 10)) // Formato YYYY-MM-DD

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
})

function openModal() {
  modal.show()
}

function increment() {
  ammount.value++
}
function decrement() {
  if (ammount.value > 0) ammount.value--
}

function handleDetail() {
  console.log({
    id_product: product.value?.id,
    recived_at: new Date().toISOString(),
    expires_at: expirationDate.value,
    ammount: ammount.value,
    cost_price: price.value,

    product: product.value,
  })
  // Aquí iría la lógica para enviar los datos al backend
  modal.hide()
}
</script>

<template>
  <button @click="openModal">mostrar</button>
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
          <div v-if="mode === 'buy'">
            <NumberInput v-model="priceBridge" :class="{ 'mb-3': true }" mode="float">
              <template #label><label class="form-label">Precio</label></template>
            </NumberInput>

            <DateInput v-model="expirationDate" v-if="product?.expires">
              <template #label><label class="form-label">Fecha de vencimiento</label></template>
            </DateInput>
          </div>
					<div v-if="mode === 'sell'">
						<p class="text-muted small">Precio unitario: {{ product?.public_price || 0 }}</p>
						<p class="text-muted small">Precio subtotal: {{ (product?.public_price || 0) * ammount }}</p>
						<p class="text-muted small">Precio total: {{ finalPrice }}</p>
					</div>
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
