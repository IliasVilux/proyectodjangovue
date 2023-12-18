<script>
import { RouterLink } from 'vue-router'
import ColaboradorCard from '../components/ColaboradorCard.vue'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'

export default {
  setup() {
    const { result } = useQuery(gql`
      query allColaboradores {
        colaboradores {
          dniCifColaborador
          nombreColaborador
        }
      }
    `)
    return {
      result
    }
  },
  components: { ColaboradorCard }
}
</script>

<template>
  <main>
    <RouterLink to="/add">Crear</RouterLink>
    <ul>
      <ColaboradorCard
        v-if="result && result.colaboradores"
        v-for="colaborador in result.colaboradores"
        :key="colaborador.dniCifColaborador"
        :dni="colaborador.dniCifColaborador"
      />
    </ul>
  </main>
</template>

<style scoped>
  ul{
    padding: 0;
  }
</style>