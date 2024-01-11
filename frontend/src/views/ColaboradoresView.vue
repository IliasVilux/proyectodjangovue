<script setup>
import { RouterLink } from 'vue-router'
import ColaboradorCard from '@/components/ColaboradorCard.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { GET_COLABORADORES } from '@/graphql/Queries/Colaboradores.js'
import { DELETE_COLABORADOR } from '@/graphql/Mutations/Colaboradores.js'
import { ApolloClient } from '@apollo/client/core'

const { result, loading, error } = useQuery(
  GET_COLABORADORES,
  {refetchQueries: ['allColaboradores']})

const { mutate: deleteColaboradorMutation } = useMutation(DELETE_COLABORADOR)

const deleteCol = (dni) => {
  deleteColaboradorMutation({
    dniCifColaborador: dni
  },
    {
      update: (cache, { data: { deleteColaborador } }) => {
        let data = cache.readQuery({ query: GET_COLABORADORES })

        const colaboradoresUpdated = data.filter(
          (colaborador) => colaborador.dniCifColaborador !== deleteColaborador.colaborador.dniCifColaborador
        );

        data = {
          colaboradoresUpdated
        }
        cache.writeQuery({ query: GET_COLABORADORES, data })
      }
    })
}
</script>

<template>
  <main>
    <RouterLink :to="{ name: 'formcolaborador' }">Crear</RouterLink>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <ul v-else-if="result && result.colaboradores">
      <ColaboradorCard v-if="result && result.colaboradores" v-for="colaborador in result.colaboradores"
        :key="colaborador.dniCifColaborador" :dni="colaborador.dniCifColaborador"
        @delete="deleteCol(colaborador.dniCifColaborador)" />
    </ul>
  </main>
</template>

<style scoped>
ul {
  padding: 0;
}
</style>
