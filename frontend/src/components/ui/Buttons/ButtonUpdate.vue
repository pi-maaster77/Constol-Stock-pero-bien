<!-- frontend/src/components/ui/Buttons/ButtonUpdate.vue -->

<template>
    <button class="bi bi-arrow-repeat btn btn-secondary" :disabled="props.disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
    disabled?: boolean
}>()
</script>