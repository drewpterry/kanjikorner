import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import Landing from './pages/Landing'
import Dashboard from './pages/Dashboard'
import ReviewDeck from './pages/ReviewDecks'
import SrsReview from './pages/SrsReview'
import VueRouter from 'vue-router'
import auth from './auth'
Vue.use(VueRouter)
Vue.use(VueResource)

/* eslint-disable no-new */
const routes = [
  { path: '/', component: Landing },
  { path: '/dashboard', component: Dashboard, meta: {requiresAuth: true} },
  { path: '/review/lvl-:lvl/:sublevel', name: 'deck', component: ReviewDeck, meta: {requiresAuth: true} },
  { path: '/review/srs', component: SrsReview, meta: {requiresAuth: true} }
]

export const router = new VueRouter({
  mode: 'history',
  routes: routes
})

router.beforeEach((to, from, next) => {
  auth.checkAuth()
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (auth.user.authenticated) {
      console.log('heere')
      next()
    } else {
      console.log('not logged in ')
      next({
        path: '/',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    next() // make sure to always call next()!
  }
})

new Vue({
  components: {App},
  template: '<App/>',
  router: router
}).$mount('#app')
