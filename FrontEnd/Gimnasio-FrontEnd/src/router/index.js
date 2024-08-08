import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterUser from '@/components/RegisterUser.vue'
import  Home from '@/components/Home.vue'
import Menu from '@/components/Menu.vue'
import Persona from '@/components/Persona.vue'
import ListaPersonas from '@/components/ListaPersonas.vue'
import Ejercicio from '@/components/Ejercicio.vue'
import Rutina from '@/components/Rutina.vue'
import ProgramaSaludable from '@/components/ProgramaSaludable.vue'
import RutinaEjercicio from '@/components/RutinaEjercicio.vue'
import DetallePrograma from '@/components/DetallePrograma.vue'

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
      component: RegisterUser
    },
    {
      path: '/home',
      name: 'home',
      component: Menu,
      children: [
        {path: '/personas', name: 'personas', component: ListaPersonas},
        {path: '/ejercicios', name: 'ejercicios', component: Ejercicio},
        {path: '/rutinas', name: 'rutinas', component: Rutina},
        {path: '/programas_saludables', name: 'programas_saludables', component: ProgramaSaludable},
        {path: '/rutinas_ejercicios', name: 'rutinas_ejercicios', component: RutinaEjercicio},
        {path: '/detalles_programas', name: 'detalles_programas', component: DetallePrograma},
      ]
    }
  ]
})

export default router
