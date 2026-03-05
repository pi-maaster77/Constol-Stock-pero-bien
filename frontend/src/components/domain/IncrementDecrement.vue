<!-- frontend/src/components/domain/IncrementDecrement.vue -->

<template>
    <NumberInputWithButtons 
        v-model="count" 
        @decrement="decrement" 
        @increment="increment"
    />
</template>

<script setup lang="ts">

import { computed } from 'vue';
import NumberInputWithButtons from '../ui/NumberInputWithButtons.vue';
import { useCounterStore } from '@/stores/counter';

const counterStore = useCounterStore()

const count = computed({
  get: () => counterStore.count,
  set: (newValue) => {
    // Aquí validamos los límites antes de guardar en el store
    if (newValue >= props.min && newValue <= props.max) {
      counterStore.count = newValue; 
      // Si tu store no permite asignación directa, usa:
      // counterStore.setCount(newValue)
    }
  }
});

const props = defineProps<{
    min: number,
    max: number
}>();

function decrement(){
    if(counterStore.count <= props.min) return
    counterStore.decrement()
}

function increment(){
    if(counterStore.count >= props.max) return
    counterStore.increment()
}

</script>