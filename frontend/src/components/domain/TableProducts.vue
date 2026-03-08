<!-- frontend/src/components/domain/TableProducts.vue -->

<template>
    <div class ="mb-3 btn-group" role="group">
        <ButtonUpdate @click="handleUpdate"/>
        <ButtonAdd @click="handleAdd" />
        <ButtonEdit @click="handleEdit" :disabled="disabled"/>
        <ButtonDelete @click="handleDelete" :disabled="disabled"/>
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
            <DumbProduct v-for="product in products" 
            :key="product.id" 
            :product="product" 
            :checked="selectedIds.includes(product.id)"
            @toggle="toggleProduct"
            />
        </tbody>
    </table>
</template>

<script setup lang="ts">    
import { ref, computed, onMounted } from 'vue';

import { useProductsStore } from '@/stores/product'
import DumbProduct from '@/components/ui/DumbProduct.vue'
import ButtonEdit from '../ui/Buttons/ButtonEdit.vue';
import ButtonDelete from '../ui/Buttons/ButtonDelete.vue';
import ButtonAdd from '../ui/Buttons/ButtonAdd.vue';
import ButtonUpdate from '../ui/Buttons/ButtonUpdate.vue';
import type { Product } from '@/types/product';

const productAtributes = ['Código de barras', 'Nombre', 'Precio', 'Cantidad']
const productStore = useProductsStore()
const { products } = productStore
const allSelected = computed(() =>
    products.length > 0 &&
    selectedIds.value.length === products.length
)
const selectedIds = ref<number[]>([])
const selectedProducts = computed(() =>
    products.filter(p => selectedIds.value.includes(p.id))
)
const disabled = computed(() => selectedIds.value.length === 0)


const emit = defineEmits<{
    (e: 'add'): void
    (e: 'edit', selectedIds: Product[]): void

}>();

function toggleAll(event: Event) {
    console.log("toggling all")
    if (allSelected.value) {
        selectedIds.value = []
    } else {
        selectedIds.value = products.map(p => p.id)
    }
}

function toggleProduct(id: number) {
    console.log("toggling product", id)
    if (selectedIds.value.includes(id)) {
        selectedIds.value = selectedIds.value.filter(p => p !== id)
    } else {
        selectedIds.value.push(id)
    }

}

onMounted(() => {
    productStore.load()
})

function handleAdd() {
    emit('add')
}
function handleEdit() {
    emit('edit', selectedProducts.value)
}
function handleDelete() {
    for (const id of selectedIds.value) {
        console.log("deleting product", id)
        productStore.deleteByID(id)
    }

}
function handleUpdate() {
    productStore.load()
}

</script>