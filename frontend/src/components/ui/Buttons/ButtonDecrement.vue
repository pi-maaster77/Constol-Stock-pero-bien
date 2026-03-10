<!-- frontend/src/components/ui/Buttons/ButtonDecrement.vue -->

<template>
  <button class="bi bi-dash-lg btn btn-danger" :disabled="disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
