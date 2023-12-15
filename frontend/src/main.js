import './assets/main.css'
import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'
import { ApolloClient, createHttpLink, InMemoryCache, gql } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'

const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/'
})
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})
const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App)
})
app.use(router)
app.mount('#app')
