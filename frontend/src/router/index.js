import { createWebHistory, createRouter } from "vue-router"
import Signup from "@/views/signup.vue"
import Login from "@/views/login.vue"



const routes = [
    {
      path: "/signup",
      name: "signup",
      component: Signup,
    },{
        path: "/login",
        name: "login",
        component: Login,
    },
  ]
  

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router