import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterUser from '@/components/RegisterUser.vue'
import  Home from '@/components/Home.vue'
import Menu from '@/components/Menu.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: RegisterUser
    },
    {
      path: '/home',
      name: 'home',
      component: Menu
    }
  ]
})

export default router
