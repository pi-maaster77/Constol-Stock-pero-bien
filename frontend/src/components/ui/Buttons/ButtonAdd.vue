<!-- frontend/src/components/ui/Buttons/ButtonAdd.vue -->

<template>
  <button class="bi bi-plus-lg btn btn-success" :disabled="disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
