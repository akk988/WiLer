import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home/Home')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/Navigation/Footer/About/About')
  },
  {
    path: '/team',
    name: 'Team',
    component: () => import('../views/Navigation/Footer/Team/Team')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/Navigation/Footer/Contact/Contact')
  },
]

const router = new VueRouter({
  routes
})

export default router
