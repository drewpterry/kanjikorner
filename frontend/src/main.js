import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'
import auth from './auth'
import VueHead from 'vue-head'
Vue.use(VueResource)
Vue.use(VueHead)

router.beforeEach((to, from, next) => {
  auth.checkAuth()
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (auth.user.authenticated) {
      next()
    } else {
      next({
        path: '/',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    next() // make sure to always call next()!
  }
})

 /* eslint-disable */
window.eventHub = new Vue()
new Vue({
  components: {App},
  template: '<App/>',
  router: router
}).$mount('#app')
