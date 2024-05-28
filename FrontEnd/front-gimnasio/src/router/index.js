import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/Login.vue'
import RegisterUser from '@/components/RegisterUser.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },

    {
      path: '/register',
      name: 'register',
      component: LoginView
    },

  ]
})

export default router
