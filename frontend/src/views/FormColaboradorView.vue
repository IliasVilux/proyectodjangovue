<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import router from '@/router'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { GET_COLABORADOR, GET_COLABORADORES } from '@/graphql/Queries/Colaboradores.js'
import { ADD_COLABORADOR, UPDATE_COLABORADOR } from '@/graphql/Mutations/Colaboradores.js'
import { useFormIdStore } from '@/store/formID.js'

var modoEdicion = false
const store = useFormIdStore()

const formData = ref({
  dniCifColaborador: '',
  nombreColaborador: ''
})

const route = useRoute()
if (route.params.dniCifColaborador || store.formDniCifColaborador) {
  store.formDniCifColaborador = route.params.dniCifColaborador

  const { result } = useQuery(
    GET_COLABORADOR,
    { dniCifColaborador: store.formDniCifColaborador }
  )

  console.log(result)
  
  formData.value.dniCifColaborador = store.formDniCifColaborador
  formData.value.nombreColaborador = result.value.colaborador.nombreColaborador

  modoEdicion = true
}

const { mutate: addColaboradorMutation } = useMutation(ADD_COLABORADOR)
const { mutate: updateColaboradorMutation } = useMutation(UPDATE_COLABORADOR)

const enviarFormulario = async () => {
  try {
    if (modoEdicion === false) {
      await addColaboradorMutation({
        dniCifColaborador: formData.value.dniCifColaborador,
        nombreColaborador: formData.value.nombreColaborador
      },
        {
          update: (cache, { data: { addColaborador } }) => {
            let data = cache.readQuery({ query: GET_COLABORADORES })
            data = {
              ...data,
              colaboradores: [
                ...data.colaboradores,
                addColaborador,
              ],
            }
            cache.writeQuery({ query: GET_COLABORADORES, data })
          }
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
    <input v-model="formData.dniCifColaborador" :disabled="modoEdicion" required />
    <input v-model="formData.nombreColaborador" required />

    <button type="submit">Agregar Colaborador</button>
  </form>
</template>

<style scoped></style>
