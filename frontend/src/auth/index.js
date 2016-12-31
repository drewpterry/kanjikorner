import {router} from '../main'

// URL and endpoint constants
const API_URL = 'api'
const LOGIN_URL = API_URL + '/rest-auth/login/'
const SIGNUP_URL = API_URL + 'users/'

export default {

  // User object will let us check authentication status
  user: {
    authenticated: false
  },

  // Send a request to the login URL and save the returned JWT
  login (context, creds, redirect) {
    console.log(router)
    context.$http.post(LOGIN_URL, creds).then((response) => {
      window.localStorage.setItem('id_token', response.data['key'])
      this.user.authenticated = true

      if (redirect) {
        router.push('/dashboard')
      }
    }, (response) => {
      console.log('failure')
    })
  },

  signup (context, creds, redirect) {
    context.$http.post(SIGNUP_URL, creds, (data) => {
      window.localStorage.setItem('id_token', data.id_token)

      this.user.authenticated = true

      if (redirect) {
        router.go(redirect)
      }
    }).error((err) => {
      context.error = err
    })
  },

  // To log out, we just need to remove the token
  logout () {
    window.localStorage.removeItem('id_token')
    this.user.authenticated = false
  },

  checkAuth () {
    var jwt = window.localStorage.getItem('id_token')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  },

  // The object to be passed as a header for authenticated requests
  getAuthHeader () {
    return {
      'Authorization': 'Token ' + window.localStorage.getItem('id_token')
    }
  }
}
