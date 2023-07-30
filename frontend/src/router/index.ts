import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import { urlPath } from '@/utils'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
      ...urlPath.HOME,
      component: () => import('../pages/Home/index.vue')
  },
    {
      ...urlPath.REGISTER,
      component: () => import('../pages/Register/index.vue')
  },
    {
      ...urlPath.LOG_IN,
      component: () => import('../pages/LogIn/index.vue')
  },
    {
      ...urlPath.FORGOT_PASSWORD,
      component: () => import('../pages/ForgotPassword/index.vue')
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
      ...urlPath.TEST,
      component: () => import('../pages/Test/index.vue')
  },
    {
      ...urlPath.QUESTION_CONTENT,
      component: () => import('../pages/Content/index.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
