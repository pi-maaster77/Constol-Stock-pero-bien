<!-- frontend/src/components/domain/CreateEditProduct.vue -->

<template>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createEditProductModal">
        Launch demo modal
    </button>
    <div class="modal fade" id="createEditProductModal" tabindex="-1" aria-labelledby="createEditProductModal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel"><span v-if="props.product">Editar</span><span v-else>Nuevo</span> Producto</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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
                        <select name="unit" id="unit" class="form-select">
                            <option>Seleccionar unidad de medida</option>
                            <option v-for="unit in units" :value="unit.id">{{ unit.name }}</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label" for="priceformula">Formula de precio</label>
                        <select name="priceformula" id="priceformula" class="form-select">
                            <option> Seleccionar formula de precio</option>
                            <option value="LIFO">LIFO</option>
                            <option value="FIFO">FIFO</option>
                            <option value="WAVG">WAVG</option>
                        </select>
                    </div>
                    <NumberInput mode="float" v-model="price" class="mb-3">
                        <template #label><label class="form-label">Precio de venta</label></template>
                    </NumberInput>
                    <div class="form-check mb-3">
                        <input type="checkbox" name="expires" id="expires" class="form-check-input">
                        <label for="expires" class="form-check-label" >
                            ¿Expira?
                        </label>
                    </div>
                </div>
                <div class="modal-footer">
                        <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>



<script setup lang="ts">

import { computed, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import NumberInput from '../ui/Inputs/NumberInput.vue';
import TextInput from '../ui/Inputs/TextInput.vue';

import type { Product } from '@/types/product';
import type { Unit } from '@/types/unit';

const counterStore = useCounterStore()
const barcode = ref(0)
const product = ref<Product | null>(null)
const price = ref(product.value?.price_cache || 0)
const units = ref<Unit[]>([])
const productName = ref('')


const props = defineProps<{
    product: Product | null
}>();


</script>