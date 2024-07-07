import { createWebHistory, createRouter } from "vue-router"
import Signup from "@/views/signup.vue"
import Login from "@/views/login.vue"
import Home from "@/views/home.vue"
import Welcome from "@/views/welcome.vue"


const routes = [
    {
      path: "/signup",
      name: "signup",
      component: Signup,
    },{
        path: "/login",
        name: "login",
        component: Login,
    },{
        path: "/",
        name: "home",
        component: Home,
    },

  ]
  

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router