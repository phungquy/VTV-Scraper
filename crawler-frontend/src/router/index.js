import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/news/:news_id',
      name: 'NewsDetails',
      component: () => import("@/views/NewsDetailsView.vue")
    },
  ]
})

export default router
