import Vue from 'vue'
import App from './App'
import Dashboard from './components/Dashboard'
import ReviewDeck from './components/ReviewDecks'
import SrsReview from './components/SrsReview'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

/* eslint-disable no-new */
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const routes = [
  { path: '/', component: Dashboard },
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
  { path: '/review/lvl-:lvl/:sublevel', component: ReviewDeck },
  { path: '/review/srs', component: SrsReview }
  // { path: '/hello', component: HelloWorld},
  // { path: '/profile/:userID', component: Bar}
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
