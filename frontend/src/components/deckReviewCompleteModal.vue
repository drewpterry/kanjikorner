<template>
<div>
  <modal v-bind:width="'800px'" @close="$emit('close')">
    <span slot="header">
      <div class="row text-center">
        <p class="red-title">Complete!</p>
      </div>
    </span>
    <form slot="body">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>#</th>
            <th>単語</th>
            <th>読み</th>
            <th>定義</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(word, index) in words">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ word.real_word }}</td>
            <td>{{ word.hiragana }}</td>
            <td>{{ word.meanings }}</td>
          </tr>
        </tbody>
      </table>
    </form>
    <form slot="footer">
      <div class="row">
        <div class="col-md-2">
          <router-link to="/dashboard">
            <p class="gray-btn text-left">Dashboard</p>
          </router>
        </div>
        <div class="col-md-3 col-md-offset-7 text-right">
          <div class="btn btn-green">Next Review</div>
        </div>
      </div>
    </form>
  </modal>
</div>
</template>

<script>
import ModalBase from './ModalBase.vue'
export default {
  name: 'completeModal',
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
  props: {
    'words': {
      required: true
    }
  },
  created () {
    console.log('yoyoy')
    console.log(this.words.length)
  },
  methods: {
    login: function () {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
</style>
