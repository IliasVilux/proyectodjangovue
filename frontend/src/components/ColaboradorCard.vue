<script setup>
defineProps({
  dni: {
    type: String,
    required: true
  },
  nombre: {
    type: String
  }
})
</script>

<template>
    <p>{{ nombre }}</p>
    <p>Dni: {{ dni }}</p>
</template>

<style scoped>
</style>