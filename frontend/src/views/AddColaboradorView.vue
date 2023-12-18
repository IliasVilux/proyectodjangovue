<script setup>
import gql from 'graphql-tag'
import { useMutation } from '@vue/apollo-composable'
import { ref } from 'vue'
import router from '@/router'

const dni_cif_colaborador = nombre = ref('')

const { mutate: agregarColaborador } = useMutation(gql`
  mutation addColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
    addColaborador(dniCifColaborador: $dniCifColaborador, nombreColaborador: $nombreColaborador) {
      colaborador {
        dniCifColaborador
        nombreColaborador
      }
    }
  }
`)

const enviarFormulario = async () => {
  try {
    await agregarColaborador({
      dniCifColaborador: dni_cif_colaborador.value,
      nombreColaborador: nombre.value
    })

    router.push({ name: 'colaboradores' })
  } catch (error) {
    console.error('Error al agregar colaborador:', error.message)
  }
}
</script>

<template>
  <form @submit.prevent="enviarFormulario">
    <label>Introduce el DNI:</label>
    <input v-model="dni_cif_colaborador" required/>

    <label>Nombre:</label>
    <input v-model="nombre" required/>

    <button type="submit">Agregar Colaborador</button>
  </form>
</template>
