<script>
import ColaboradorCard from '../components/ColaboradorCard.vue';
import gql from 'graphql-tag';

export default {
    apollo: {
        colaboradores: gql `
      query {
        colaboradores {
          dniCifColaborador 
          nombreColaborador
        }
      }
    `,
    },
    data() {
        return {
            colaborador: null,
        };
    },
    components: { ColaboradorCard }
};
</script>

<template>
  <main>
    <div v-for="colaborador in colaboradores" :key="colaborador.dniCifColaborador">
      <ColaboradorCard :dni="colaborador.dniCifColaborador" :nombre="colaborador.nombreColaborador"/>
    </div>
  </main>
</template>
