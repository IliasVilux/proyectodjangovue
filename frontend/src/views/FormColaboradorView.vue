<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'

const dniCifColaborador = ref('')
const nombre = ref('')

onMounted(() => {
  const route = useRoute()
  if (route.params.dniCifColaborador) {
    dniCifColaborador.value = route.params.dniCifColaborador

    const { result } = useQuery(
      gql`
        query colaborador($dniCifColaborador: String!) {
          colaborador(dniCifColaborador: $dniCifColaborador) {
            dniCifColaborador
            nombreColaborador
            apellidosColaborador
          }
        }
      `,
      { dniCifColaborador: dniCifColaborador.value }
    )
    nombre.value = result.value.colaborador.nombreColaborador
  }
})
</script>

<template>
  <form @submit.prevent="enviarFormulario">
    <input v-model="dniCifColaborador" required />
    <input v-model="nombre" required />

    <button type="submit">Agregar Colaborador</button>
  </form>
</template>

<style scoped></style>
