<!-- frontend/src/components/ui/Buttons/ButtonExport.vue -->

<!-- frontend/src/components/ui/Buttons/ButtonUpdate.vue -->

<template>
  <button class="bi bi-arrow-bar-right btn btn-primary" :disabled="props.disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
