import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/listaklient.vue'
import Customers from '../views/listaklient.vue';
import Customer from '../views/klient.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/klient.vue')
    },
    {
      path: '/',
      component: Customers
    }
    ,
    {
      path: '/customers/:id',
      name:  'customer',
      component: Customers
    }
  ]
})

export default router
