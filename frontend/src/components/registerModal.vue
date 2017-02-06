<template>
<div>
  <modal @close="$emit('close')">
    <span slot="header">
      登録 (Registration)
    </span>
    <form slot="body">
      <div v-show="!success">
        <input v-model="username" type="text" placeholder="username" class="c-textarea"> 
        {{ error.username }}
        <input v-model="email" type="text" placeholder="email" class="c-textarea"> 
        {{ error.email }}
        <input v-model="password" type="password" placeholder="password" class="c-textarea"> 
        {{ error.password1 }}
        <input v-model="passwordConfirm" type="password" placeholder="confirm password" class="c-textarea"> 
        {{ error.password2 }}
      </div>
        {{ success }}
    </form>
    <form v-show="!success" slot="footer">
      <div v-on:click="register" class="btn btn-green">ok</div>
    </form>
  </modal>
</div>
</template>

<script>
import ModalBase from './ModalBase.vue'
export default {
  name: 'registrationModal',
  data () {
    return {
      error: '',
      success: null,
      username: '',
      email: '',
      password: '',
      passwordConfirm: ''
    }
  },
  components: {
    'modal': ModalBase
  },
  methods: {
    register: function () {
      var userInfo = {
        email: this.email,
        username: this.username,
        password1: this.password,
        password2: this.passwordConfirm
      }
      this.registerPost(userInfo)
    },
    registerPost: function (userInfo) {
      var url = '/api/rest-auth/registration/'
      this.$http.post(url, userInfo)
      .then(response => {
        this.success = 'Cool! Check your email to verify your account.'
      }, error => {
        if (error) {
          this.error = error.body
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../assets/style/landing-page-css/style.scss";

</style>
