<!-- frontend/src/components/domain/DiscountTable.vue -->

<script setup lang="ts">
import { useDiscountsStore } from '@/stores/discount';
import DumbDiscount from '../ui/DumbDiscount.vue';
import { useProductsStore } from '@/stores/product';
import { computed, onMounted, ref } from 'vue';
import ButtonUpdate from '../ui/Buttons/ButtonUpdate.vue';
import ButtonAdd from '../ui/Buttons/ButtonAdd.vue';
import ButtonEdit from '../ui/Buttons/ButtonEdit.vue';
import ButtonDelete from '../ui/Buttons/ButtonDelete.vue';


const discountStore = useDiscountsStore()
const productStore = useProductsStore()
const productAtributes = [
	"Codigo de barras", "Nombre", "Cantidad Minima", "Descuento"
]

const selectedIds = ref<number[]>([])
const allSelected = computed(  
	() => discountStore.discountsCount > 0 && selectedIds.value.length === discountStore.discountsCount,
)
const disabled = computed(()=> selectedIds.value.length === 0)

const emit = defineEmits<{
  (e: 'add'): void
  (e: 'edit', selectedIds: number[]): void
}>()

function toggleAll(){
	selectedIds.value = discountStore.discounts.map(d => d.id)
}

function handleUpdate(){
	discountStore.load()
}
function handleAdd(){
	emit('add')
}
function handleEdit(){
	emit('edit', selectedIds.value)
}
function handleDelete(){
	for(const discount of selectedIds.value){
		discountStore.deleteByID(discount)
	}
}

onMounted(
	()=>discountStore.load()
)
</script>

<template>
	<div class="container mt-4">
    <h3 class="mb-3">Lista de productos</h3>
    <div class="mb-3 btn-group" role="group">
      <ButtonUpdate @click="handleUpdate" />
      <ButtonAdd @click="handleAdd" />
      <ButtonEdit @click="handleEdit" :disabled="disabled" />
      <ButtonDelete @click="handleDelete" :disabled="disabled" />
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
					<th 
						v-for="header in productAtributes" 
						:key="header"
					>
						{{ header }}
					</th>
				</tr>
			</thead>
			<tbody>
				<DumbDiscount 
					:product="productStore.getProductByID(discount.id_product)"
					:ammount="discount.min_ammount"
					:id="discount.id"
					:percent="discount.discount"
					:checked="discount.id in selectedIds"
					v-for="discount in discountStore.discounts"
				
				/>
			</tbody>
		</table>
	</div>
</template>