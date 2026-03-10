<!-- frontend/src/components/ui/Buttons/ButtonEdit.vue -->

<template>
  <button class="bi bi-pencil-fill btn btn-primary" :disabled="props.disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
