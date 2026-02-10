<!-- frontend/src/App.vue -->

<script setup lang="ts">

import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import IncrementarDecrementar from '@/components/domain/IncrementarDecrementar.vue';

</script>

<template>
  <IncrementarDecrementar :min="0" :max="100"/>
</template>