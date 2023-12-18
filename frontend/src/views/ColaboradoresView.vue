<script>
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
