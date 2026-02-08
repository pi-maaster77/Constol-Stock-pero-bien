<template>
    <span class="input-group">
        <NumberInput
            :modelValue="modelValue"
            @update:modelValue="change" 
        />
        <ButtonIncrement @click="increment" />
        <ButtonDecrement @click="decrement" />
    </span>
</template>

<script setup lang="ts">
import ButtonDecrement from '../ui/ButtonDecrement.vue';
import ButtonIncrement from '../ui/ButtonIncrement.vue';
import NumberInput from '../ui/NumberInput.vue';

defineProps<{
    modelValue: number | string
}>();

const emit = defineEmits(['increment', 'decrement', 'update:modelValue'])

function increment(){
    emit('increment')
}

function decrement(){
    emit('decrement')
}

// 2. El evento que viene de NumberInput ya es el valor, no el objeto Event
function change(value: string | number){
    emit('update:modelValue', value)
}
</script>