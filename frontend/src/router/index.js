import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/WelcomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    meta: { title: 'Drip Search' },
    component: HomePage
  },
  {
    path: '/Search:query',
    name: 'Playground',
    params: true,
    meta: { title: 'Search' },
    component: () => import(/* webpackChunkName: "Playground" */ '../views/Search.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
