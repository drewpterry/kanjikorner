import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import Dashboard from './components/Dashboard'
import ReviewDeck from './components/ReviewDecks'
import SrsReview from './components/SrsReview'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
Vue.use(VueResource)

/* eslint-disable no-new */
const routes = [
  { path: '/', component: Dashboard },
  { path: '/review/lvl-:lvl/:sublevel', name: 'deck', component: ReviewDeck },
  { path: '/review/srs', component: SrsReview }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

new Vue({
  components: {App},
  template: '<App/>',
  router: router
}).$mount('#app')
