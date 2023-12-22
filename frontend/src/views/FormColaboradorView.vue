<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import router from '@/router'
import gql from 'graphql-tag'
import { useQuery, useMutation } from '@vue/apollo-composable'

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
    nombreColaborador.value = result.value.colaborador.nombreColaborador
    entryData.value.nombreColaborador = route.params.nombreColaborador

    modoEdicion = true
  }
})

const { mutate: addColaboradorMutation } = useMutation(
  gql`
    mutation addColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
      addColaborador(dniCifColaborador: $dniCifColaborador, nombreColaborador: $nombreColaborador) {
        colaborador {
          dniCifColaborador
          nombreColaborador
        }
      }
    }
  `,
  () => ({
    update(cache, { data: { addColaborador } }) {
      cache.writeQuery({
        query: gql`
          query allColaboradores {
            colaboradores {
              dniCifColaborador
              nombreColaborador
            }
          }
        `,
        data: {
          colaboradores: addColaborador
        }
      })
    }
  })
)

const { mutate: updateColaboradorMutation } = useMutation(
  gql`
    mutation updateColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
      updateColaborador(
        dniCifColaborador: $dniCifColaborador
        nombreColaborador: $nombreColaborador
      ) {
        colaborador {
          dniCifColaborador
          nombreColaborador
        }
      }
    }
  `)

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
