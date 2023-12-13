<script>
import gql from 'graphql-tag';

export default {
  apollo: {
    colaborador: gql`
      query {
        colaborador(dniCifColaborador: "99999999M") {
          dniCifColaborador 
          nombreColaborador
        }
      }`,
  },
  data() {
    return {
      colaborador: null,
    };
  },
};
</script>



<template>
  <main>
    <!-- <ColaboradorCard dni="999999I" nombre="Ilias"/>
    <ColaboradorCard dni="123345678" nombre="Otro Usuario"/> -->
  </main>
</template>
