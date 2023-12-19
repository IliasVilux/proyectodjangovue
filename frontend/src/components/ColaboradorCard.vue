<script setup>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import DeleteColaboradorButton from './DeleteColaboradorButton.vue'
import UpdateColaboradorButton from './UpdateColaboradorButton.vue'

const props = defineProps({
  dni: {
    type: String,
    required: true
  }
})

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
  { dniCifColaborador: props.dni }
)
</script>

<template>
  <div v-if="result && result.colaborador" class="colaboradorCard">
    <div>
      <p>
        {{ result.colaborador.nombreColaborador }} {{ result.colaborador.apellidosColaborador }}
      </p>
      <p style="color: #9aa0a6">{{ result.colaborador.dniCifColaborador }}</p>
    </div>
    <div>
      <UpdateColaboradorButton :dniCifColaborador="result.colaborador.dniCifColaborador"/>
      <DeleteColaboradorButton :dniCifColaborador="result.colaborador.dniCifColaborador"/>
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
