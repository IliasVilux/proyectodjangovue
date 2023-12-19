<script setup>
import gql from 'graphql-tag'
import { useMutation, useQuery } from '@vue/apollo-composable'
import { ref, onMounted } from 'vue'
import router from '@/router'

const props = defineProps({
  modo: {
    type: String,
    default: 'add'
  },
  dniCifColaboradorInput: String
})


const dni_cif_colaborador = ref(props.dniCifColaboradorInput)

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

const { mutate: updateColaborador } = useMutation(gql`
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
    if (props.modo === 'add') {
      await agregarColaborador({
        dniCifColaborador: dni_cif_colaborador.value,
        nombreColaborador: nombre.value
      })
    } else {
      await updateColaborador({
        dniCifColaborador: dniCifColaboradorInput.value,
        nombreColaborador: nombre.value
      })
    }

    router.push({ name: 'colaboradores' })
  } catch (error) {
    console.error('Error al agregar colaborador:', error.message)
  }
}
</script>

<template>
  <div>
    <form @submit.prevent="enviarFormulario">
      <label>Introduce el DNI:</label>
      <input v-model="dni_cif_colaborador" required :disabled="modo === 'editar'" />

      <label>Nombre:</label>
      <input v-model="nombre" required />

      <button type="submit">Agregar Colaborador</button>
    </form>
  </div>
</template>

<style scoped>
form {
  max-width: 400px;
  margin: auto;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  box-sizing: border-box;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 10px 15px -3px;
  margin-bottom: 10px;
}

button {
  color: white;
  background-color: #00bd7e;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 16px;
}
</style>
