import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ColaboradoresView from '../views/ColaboradoresView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/colaboradores',
      name: 'colaboradores',
      component: ColaboradoresView
    }
  ]
})

export default router
