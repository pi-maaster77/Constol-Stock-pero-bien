<!-- frontend/src/components/domain/DiscountMenu.vue -->

<!-- frontend/src/components/domain/DicountMenu.vue -->

<script setup lang="ts">
import { getProductByBC } from '@/api/product'
import { useDiscountsStore } from '@/stores/discount'
import type { Product } from '@/types/product'
import type { Discount } from '@/types/discounts'
import { Modal } from 'bootstrap'
import { computed, onMounted, ref, watch } from 'vue'
import NumberInputWithButtons from '../ui/Inputs/NumberInputWithButtons.vue'
import TextInput from '../ui/Inputs/TextInput.vue'
import NumberInput from '../ui/Inputs/NumberInput.vue'
import PercentInput from '../ui/Inputs/PercentInput.vue'
import { useProductsStore } from '@/stores/product'

const props = defineProps<{
	discount?:  Discount
}>()

const discountStore = useDiscountsStore()
const productStore = useProductsStore()

const barcode = ref<string>('')
const product = ref<Product | null>(null)
const displayName = computed(
  () => product.value ? product.value.name : ''
)
const isLoading = ref<boolean>(false)
const productNotFound = ref<boolean>(false)
const ammount = ref(0)
const ammountBridge = computed({
  get: () => ammount.value.toString(),
  set: (val) => {
    ammount.value = parseFloat(val) || 0
  },
})
const discountPercent = ref(0)
const discountPercentBridge = computed({
  get: () => discountPercent.value.toString(),
  set: (val) => {
    discountPercent.value = parseFloat(val) || 0
  },
})
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

watch(
  () => props.discount,
  (d) => {
    if (!d) return
		const tempProduct = productStore.getProductByID(d.id_product)
		if (!tempProduct) return
    product.value = tempProduct
		barcode.value = tempProduct.bc
    ammount.value = d.min_ammount
		discountPercent.value = d.discount*100 
	},
  { immediate: true },
)

let modal: Modal

onMounted(() => {
  const el = document.getElementById('DiscountModal')
  modal = new Modal(el!)
})

function openModal(){
	modal.show()
}

function closeModal() {
	modal.hide()
}

function increment(){
	ammount.value++
}

function decrement(){
	if(ammount.value > 0 ){
		ammount.value--
	}
}

function handleDetail() {
  if (product.value !== undefined && product.value !== null) {
    discountStore.create({
      min_ammount: ammount.value,
      id_product: product.value.id,
			discount: discountPercent.value/100
    })
  }
  closeModal()
}

function handleSave() {
	if(!product.value || !props.discount) return
	discountStore.updateByID(
		props.discount.id,
		{
			id_product: product.value.id,
			min_ammount: ammount.value,
			discount: discountPercent.value/100
		}
	)
  closeModal()
}

defineExpose({
  openModal,
})

</script>

<template>
  <div
    class="modal fade"
    id="DiscountModal"
    tabindex="-1"
    aria-labelledby="DiscountModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">
						<span v-if="discount">Editar</span><span v-else>Crear</span> Descuento
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
						:disabled="props.discount !== null"
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
					<PercentInput
						v-model="discountPercentBridge"
						:class="{ 'mb-3': true }"
					>
						<template #label><label class="form-label">Descuento</label></template>
					</PercentInput>
          <div class="modal-footer">
						<button type="button" class="btn btn-primary" @click="handleSave" v-if="props.discount">Guardar</button>
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
