<!-- frontend/src/components/domain/CreateEditProduct.vue -->

<template>
  <div
    class="modal fade"
    id="createEditProductModal"
    tabindex="-1"
    aria-labelledby="createEditProductModal"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">
            <span v-if="props.product">Editar</span><span v-else>Nuevo</span> Producto
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <NumberInput mode="barcode" v-model="barcode" class="mb-3">
            <template #label><label class="form-label">Codigo de barras</label></template>
          </NumberInput>
          <TextInput v-model="productName" class="mb-3">
            <template #label><label class="form-label">Nombre</label></template>
          </TextInput>
          <div class="mb-3">
            <label class="form-label" for="unit">Unidad de medida</label>
            <select name="unit" id="unit" class="form-select" v-model="productUnit">
              <option v-for="unit in units" :value="unit.id">{{ unit.name }}</option>
            </select>
          </div>
          <div class="mb-3">
            <label class="form-label" for="priceformula">Formula de precio</label>
            <select
              name="priceformula"
              id="priceformula"
              class="form-select"
              v-model="priceFormula"
            >
              <option value="LIFO">LIFO</option>
              <option value="FIFO">FIFO</option>
              <option value="WAVG">WAVG</option>
            </select>
          </div>
          <NumberInput mode="float" v-model="price" class="mb-3">
            <template #label><label class="form-label">Precio de venta</label></template>
          </NumberInput>
          <div class="form-check mb-3">
            <input
              type="checkbox"
              name="expires"
              id="expires"
              class="form-check-input"
              v-model="expires"
            />
            <label for="expires" class="form-check-label"> ¿Expira? </label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="save" v-if="props.product">
            Guardar
          </button>
          <button type="button" class="btn btn-primary" @click="create" v-else>Crear</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Modal } from 'bootstrap'
import { computed, onMounted, ref } from 'vue'
import NumberInput from '../ui/Inputs/NumberInput.vue'

import type { Product } from '@/types/product'
import type { Unit } from '@/types/unit'
import TextInput from '../ui/Inputs/TextInput.vue'
import { useUnitsStore } from '@/stores/units'
import { useProductsStore } from '@/stores/product'
import { watch } from 'vue'
import { createAbstractBuilder } from 'typescript'
const props = defineProps<{
  product: Product | null
}>()

const units = ref<Unit[]>([])

watch(
  () => props.product,
  (p) => {
    if (!p) return

    barcode.value = p.bc
    productName.value = p.name
    productUnit.value = p.unit_id
    priceFormula.value = p.price_formula
    price.value = p.public_price
    expires.value = p.expires
  },
  { immediate: true },
)

const barcode = ref(props.product?.bc || '0')
const productName = ref(props.product?.name || '')
const productUnit = ref(props.product?.unit_id || null)
const priceFormula = ref(props.product?.price_formula || undefined)
const price = ref(props.product?.public_price || 0)
const expires = ref(props.product?.expires || false)

const unitsStore = useUnitsStore()
const productStore = useProductsStore()
onMounted(() => {
  unitsStore.load()
  units.value = unitsStore.units
  console.log('units', units.value)
})

let modal: Modal

onMounted(() => {
  const el = document.getElementById('createEditProductModal')
  modal = new Modal(el!)
})

defineExpose({
  openModal,
})

function openModal() {
  modal.show()
}

function save() {
  console.log({
    barcode: barcode.value.toString(),
    name: productName.value,
    unit_id: productUnit.value,
    price_formula: priceFormula.value,
    public_price: price.value,
    expires: expires.value,
  })
  productStore.updateByID(props.product!.id, {
    bc: barcode.value.toString(),
    name: productName.value,
    unit_id: productUnit.value!,
    price_formula: priceFormula.value as 'LIFO' | 'FIFO' | 'WAVG',
    public_price: price.value,
    expires: expires.value,
    ammount: 0,
    price_cache: null,
  })

  modal.hide()
}

function create() {
  console.log({
    barcode: barcode.value.toString(),
    name: productName.value,
    unit_id: productUnit.value,
    price_formula: priceFormula.value,
    public_price: price.value,
    expires: expires.value,
  })
  productStore.create({
    bc: barcode.value.toString(),
    name: productName.value,
    unit_id: productUnit.value!,
    price_formula: priceFormula.value as 'LIFO' | 'FIFO' | 'WAVG',
    public_price: price.value,
    expires: expires.value,
    ammount: 0,
    price_cache: null,
  })

  barcode.value = '0'
  productName.value = ''
  productUnit.value = null
  priceFormula.value = undefined
  price.value = 0
  expires.value = false

  modal.hide()
}
</script>
