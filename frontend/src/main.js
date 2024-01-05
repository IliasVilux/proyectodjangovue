import './assets/main.css'
import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'

const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/'
})
const typePolicies = {
  ColaboradorType: {
    keyFields: ['dniCifColaborador']
  },
  fields: {
    colaboradores: {
      merge(existing = [], incoming) {
        return [...existing, ...incoming];
      }
    }
  }
}

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache({ typePolicies })
})

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App)
})
app.use(router)
app.mount('#app')
