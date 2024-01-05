<script setup>
import DeleteColaboradorButton from './DeleteColaboradorButton.vue'
import UpdateColaboradorButton from './UpdateColaboradorButton.vue'
import { defineEmits } from 'vue';
import { useQuery } from '@vue/apollo-composable'
import { GET_COLABORADOR } from '../graphql/Queries/Colaboradores.js'

const props = defineProps({
  dni: {
    type: String,
    required: true
  }
})
const { result, loading, error } = useQuery(
  GET_COLABORADOR,
  { dniCifColaborador: props.dni }
)

const emits = defineEmits(
  ['delete']
)
const handleCkick = () => {
  emits('delete')
}
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-if="error">Oh no... {{ error }}</div>
  <div v-if="result && result.colaborador" class="colaboradorCard">
    <div>
      <p>
        {{ result.colaborador.nombreColaborador }} {{ result.colaborador.apellidosColaborador }}
      </p>
      <p style="color: #9aa0a6">{{ result.colaborador.dniCifColaborador }}</p>
    </div>
    <div>
      <UpdateColaboradorButton :dniCifColaborador="result.colaborador.dniCifColaborador" />
      <DeleteColaboradorButton :dniCifColaborador="result.colaborador.dniCifColaborador" @delete="handleCkick" />
    </div>
  </div>
</template>

<style>
.colaboradorCard {
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  padding: 10px;
  margin: 10px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 10px 15px -3px;
}

button {
  background-color: white;
  border-radius: 8px;
  padding: 10px;
  transition: 0.3s ease;
  cursor: pointer;
}
</style>
