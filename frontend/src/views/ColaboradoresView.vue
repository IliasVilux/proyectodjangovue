<script>
import gql from 'graphql-tag'

export default {
  name: 'Home',
  apollo: {
    colaboradores: {
      query: gql`
        query {
          colaboradores {
            dniCifColaborador
            nombreColaborador
            apellidosColaborador
          }
        }
      `
    }
  }
}
</script>

<template>
  <main>
    <div
      v-for="colaborador in colaboradores"
      :key="colaborador.dniCifColaborador"
    >
      {{ colaborador }}
    </div>
    <!-- <ColaboradorCard dni="999999I" nombre="Ilias"/>
    <ColaboradorCard dni="123345678" nombre="Otro Usuario"/> -->
  </main>
</template>
