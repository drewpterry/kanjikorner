import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

import Landing from '../pages/Landing'
import Dashboard from '../pages/Dashboard'
import ReviewDeck from '../pages/ReviewDecks'
import SrsReview from '../pages/SrsReview'

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Landing },
    { path: '/dashboard', component: Dashboard, meta: {requiresAuth: true} },
    { path: '/review/lvl-:lvl/:sublevel', name: 'deck', component: ReviewDeck, meta: {requiresAuth: true} },
    { path: '/review/srs', component: SrsReview, meta: {requiresAuth: true} }
  ]
})
