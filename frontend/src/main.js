import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import Landing from './pages/Landing'
import Dashboard from './pages/Dashboard'
import ReviewDeck from './pages/ReviewDecks'
import SrsReview from './pages/SrsReview'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
Vue.use(VueResource)

/* eslint-disable no-new */
const routes = [
  { path: '/', component: Landing },
  { path: '/dashboard', component: Dashboard },
  { path: '/review/lvl-:lvl/:sublevel', name: 'deck', component: ReviewDeck },
  { path: '/review/srs', component: SrsReview }
]

export const router = new VueRouter({
  mode: 'history',
  routes: routes
})

new Vue({
  components: {App},
  template: '<App/>',
  router: router
}).$mount('#app')
