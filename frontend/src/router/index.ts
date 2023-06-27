import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import { urlPath } from '@/utils/'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
      ...urlPath.HOME,
      component: () => import('../pages/Home/index.vue')
  },
  {
      ...urlPath.LOOK_UP,
      component: () => import('../pages/LookUp/index.vue')
  },
  {
      ...urlPath.PRACTICE,
      component: () => import('../pages/Practice/index.vue')
  },
  {
      ...urlPath.RANKING,
      component: () => import('../pages/Ranking/index.vue')
  },
  {
      ...urlPath.STATISTICS,
      component: () => import('../pages/Statistics/index.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
