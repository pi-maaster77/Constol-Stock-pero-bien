<!-- frontend/src/components/ui/Buttons/ButtonAccept.vue -->

<template>
  <button class="bi bi-check-lg btn btn-info" :disabled="disabled"></button>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean
}>()
</script>
