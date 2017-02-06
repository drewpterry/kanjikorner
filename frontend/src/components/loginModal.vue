<template>
<div>
  <modal @close="$emit('close')">
    <span slot="header">
     ログイン 
    </span>
    <form slot="body">
      <input v-model="email" type="text" placeholder="email" class="c-textarea"> 
      <input v-model="password" type="password" placeholder="password" class="c-textarea"> 
      {{ error }}
    </form>
    <form slot="footer">
      <div v-on:click="login" class="btn btn-green">login</div>
    </form>
  </modal>
</div>
</template>

<script>
import ModalBase from './ModalBase.vue'
import auth from '../auth'
export default {
  name: 'loginModal',
  data () {
    return {
      error: null,
      email: '',
      password: ''
    }
  },
  components: {
    'modal': ModalBase
  },
  methods: {
    login: function () {
      var credentials = {
        email: this.email,
        password: this.password
      }
      auth.login(this, credentials, '/dashboard')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../assets/style/landing-page-css/style.scss";

</style>
