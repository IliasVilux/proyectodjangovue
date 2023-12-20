<script setup>
import { RouterLink } from 'vue-router'
import ColaboradorCard from '../components/ColaboradorCard.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'

const { result } = useQuery(gql`
  query allColaboradores {
    colaboradores {
      dniCifColaborador
      nombreColaborador
    }
  }
`)

const { mutate: deleteColaboradorMutation } = useMutation(
  gql`
    mutation deleteColaborador($dniCifColaborador: String!) {
      deleteColaborador(dniCifColaborador: $dniCifColaborador) {
        colaborador {
          dniCifColaborador
          nombreColaborador
        }
      }
    }
  `,
  () => ({
    update(cache, { data: { deleteColaborador } }) {
      const data = cache.readQuery({
        query: gql`
          query allColaboradores {
            colaboradores {
              dniCifColaborador
              nombreColaborador
            }
          }
        `
      })

      const updatedColaboradores = data.colaboradores.filter(
        (colaborador) => colaborador.dniCifColaborador !== deleteColaborador.colaborador.dniCifColaborador
      )
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
          colaboradores: updatedColaboradores
        }
      })
    }
  })
)

const deleteCol = (dni) => {
  deleteColaboradorMutation({ dniCifColaborador: dni })
}
</script>

<template>
  <main>
    <RouterLink :to="{ name: 'formcolaborador' }">Crear</RouterLink>
    <ul>
      <ColaboradorCard
        v-if="result && result.colaboradores"
        v-for="colaborador in result.colaboradores"
        :key="colaborador.dniCifColaborador"
        :dni="colaborador.dniCifColaborador"
        @delete="deleteCol(colaborador.dniCifColaborador)"
      />
    </ul>
  </main>
</template>

<style scoped>
ul {
  padding: 0;
}
</style>
