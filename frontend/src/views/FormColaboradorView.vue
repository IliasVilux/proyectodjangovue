<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import router from '@/router'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { GET_COLABORADORES, GET_COLABORADOR } from '@/graphql/Queries/Colaboradores.js'
import { ADD_COLABORADOR, UPDATE_COLABORADOR } from '@/graphql/Mutations/Colaboradores.js'
import { gql } from '@apollo/client/core'

var modoEdicion = false // false en caso de crear, true en caso de modificar a un colaborador

// Variable to check if there been some changes
const entryData = ref({
  dniCifColaborador: '',
  nombreColaborador: ''
})

const dniCifColaborador = ref('')
const nombreColaborador = ref('')

onMounted(() => {
  const route = useRoute()
  if (route.params.dniCifColaborador) {
    dniCifColaborador.value = route.params.dniCifColaborador
    entryData.value.dniCifColaborador = route.params.dniCifColaborador

    const { result } = useQuery(
      GET_COLABORADOR,
      { dniCifColaborador: dniCifColaborador.value }
    )
    nombreColaborador.value = result.value.colaborador.nombreColaborador
    entryData.value.nombreColaborador = route.params.nombreColaborador

    modoEdicion = true
  }
})

const { mutate: addColaboradorMutation } = useMutation(
  ADD_COLABORADOR,
  // () => ({
  //   update(cache, { data: { addColaborador } }) {
  //     cache.modify({
  //       fields: {
  //         colaboradores(existingColaboradores = []) {
  //           const newColaboradorRef = cache.writeFragment({
  //             data: addColaborador,
  //             fragment: gql`
  //             fragment NewColaborador on ColaboradorType {
  //               dniCifColaborador
  //               type
  //             }`
  //           })
  //           return [...existingColaboradores, newColaboradorRef]
  //         }
  //       }
  //     })
  //   }
  // })
)
const { mutate: updateColaboradorMutation } = useMutation(UPDATE_COLABORADOR)

const enviarFormulario = async () => {
  try {
    if (modoEdicion === false) {
      await addColaboradorMutation({
        dniCifColaborador: dniCifColaborador.value,
        nombreColaborador: nombreColaborador.value
      })
    } else {
      await updateColaboradorMutation({
        dniCifColaborador: dniCifColaborador.value,
        nombreColaborador: nombreColaborador.value
      })
    }

    router.push({ name: 'colaboradores' })
  } catch (error) {
    console.error(
      'Error al agregar colaborador o modificar el colaborador con DNI: ' + dniCifColaborador.value + " - Error: ",
      error.message
    )
  }
}
</script>

<template>
  <form @submit.prevent="enviarFormulario">
    <input v-model="dniCifColaborador" :disabled="modoEdicion" required />
    <input v-model="nombreColaborador" required />

    <button type="submit">Agregar Colaborador</button>
  </form>
</template>

<style scoped></style>
