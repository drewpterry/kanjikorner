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
          <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
          </tr>
          <tr>
            <th scope="row">4</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
          </tr>
          <tr>
            <th scope="row">5</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>
    </form>
    <form slot="footer">
      <div class="row">
        <div class="col-md-2">
          <a href=""><p class="gray-btn text-left">Home page</p></a>
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
  methods: {
    login: function () {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
</style>
