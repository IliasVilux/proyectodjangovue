<script setup>
import { RouterLink } from 'vue-router'
import ColaboradorCard from '../components/ColaboradorCard.vue'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'

const { result } = useQuery(gql`
  query allColaboradores {
    colaboradores {
      dniCifColaborador
      nombreColaborador
    }
  }
`)
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
      />
    </ul>
  </main>
</template>

<style scoped>
ul {
  padding: 0;
}
</style>
