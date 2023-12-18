<script setup>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useMutation } from '@vue/apollo-composable'

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

const { mutate: deleteColaborador } = useMutation(gql`
  mutation deleteColaborador($dniCifColaborador: String!) {
    deleteColaborador(dniCifColaborador: $dniCifColaborador) {
      message
    }
  }
`)
</script>

<template>
  <div v-if="result && result.colaborador" class="colaboradorCard">
    <div>
      <p>
        {{ result.colaborador.nombreColaborador }} {{ result.colaborador.apellidosColaborador }}
      </p>
      <p>{{ result.colaborador.dniCifColaborador }}</p>
    </div>
    <div>
      <button class="editBtn">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-pencil"
          viewBox="0 0 16 16"
        >
          <path
            d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"
          />
        </svg>
      </button>
      <button
        class="deleteBtn"
        @click="deleteColaborador({ dniCifColaborador: result.colaborador.dniCifColaborador })"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="#ff000f"
          class="bi bi-trash3"
          viewBox="0 0 16 16"
        >
          <path
            d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
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
.editBtn {
  border: 1px solid rgba(0, 0, 0, 0.2);
  margin-right: 2px;
}
.deleteBtn {
  border: 1px solid rgba(255, 0, 0, 0.2);
  margin-left: 2px;
}

/* HOVER */
.editBtn:hover {
  background-color: black;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}
.editBtn:hover svg,
.deleteBtn:hover svg {
  fill: #ffffff;
}
.editBtn svg {
  fill: #333333;
}

.deleteBtn:hover {
  background-color: #ff000f;
  box-shadow: 0 0 15px rgba(255, 0, 15, 0.3);
}
</style>
