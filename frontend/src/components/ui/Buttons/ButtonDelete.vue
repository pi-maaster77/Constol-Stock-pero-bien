<!-- frontend/src/components/ui/Buttons/ButtonDelete.vue -->

<template>
  <button class="bi bi-trash-fill btn btn-danger" :disabled="props.disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
