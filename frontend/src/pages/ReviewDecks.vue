<template>
<div class="internal-page">
  <div class="green-cover">
    <div class="row green-cover__head">
      <div class="col-md-2 col-sm-1">
        <router-link to="/">
          <div class="logo">
            <img src="../assets/img/logo-white.svg" alt="">
          </div>
        </router-link>
      </div>
      <div class="col-md-offset-9 col-md-1">
        <p class="green-cover__progress">2 / 20</p>
      </div>
    </div>
    <div class="container green-cover__body">
      <div class="row ">
        <div class="col-md-offset-2 col-md-8">
         <card v-if="initialFetchComplete" v-bind:words="reviewDeck" v-bind:deck="true"></card>
        </div>
      </div>
    </div>
  </div>
  <div class="lesson">
    <div class="row">
      <div class="col-md-4">
        <p class="red-title">Basics</p>
        <div class="row lesson__row">
          <div class="col-md-3">
            <p class="gray-title">Reading:</p>
          </div>
          <div class="col-md-9">
            <p class="simple-text">Mauris non tempor quam</p>
          </div>
        </div>
        <div class="row lesson__row">
          <div class="col-md-3">
            <p class="gray-title">POS:</p>
          </div>
          <div class="col-md-9">
            <p class="simple-text">Noun, no-adjective</p>
          </div>
        </div>
        <div class="row lesson__row">
          <div class="col-md-3">
            <p class="gray-title">Kanji:</p>
          </div>
          <div class="col-md-9">
            <div class="panel text-center">
              大
              <p class="gray-title">big</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4 lesson__center">
        <p class="red-title">Details</p>
        <p class="gray-title">Meanings:</p>
        <p class="simple-text">Presidend, persin in charge, leader</p><br>
        <p class="gray-title">Sentences:</p><br>
        <p class="simple-text">1. Nam dapibus nisl vitae elit fringilla rutrum.</p><br><br>
        <p class="simple-text">2. Aenean sollicitudin, erat a elementum rutrum, neque sem pretium metus, quis mollis nisl.</p>
      </div>
      <div class="col-md-4">
        <p class="red-title">The good stuff</p>
        <p class="lesson__question">When most frequently heard?</p>
        <p class="simple-text">Fusce vehicula dolor arcu, sit amet blandit dolor mollis nec.</p><br>
        <p class="lesson__question">When not to use?</p>
        <p class="simple-text">Fusce vehicula dolor arcu, sit amet blandit dolor mollis nec.</p>
      </div>
 
    </div>
  </div>
 
  <!-- Modal -->
  <div class="modal fade" id="completeModal" role="dialog">
    <div class="modal-dialog">
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-body">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <div class="row text-center">
            <p class="red-title">Complete!</p>
          </div>
          <table class="table table-striped">
            <tr>
              <td>大</td>
              <td style="width: 30%">遊戲進入每一課。</td>
              <td>
                Mauris non tempor quam, et lacinia sapien
                auris accumsan eros
              </td>
            </tr>
            <tr>
              <td>大</td>
              <td>遊戲進入每一課。</td>
              <td>
                Mauris non tempor quam, et lacinia sapien
                auris accumsan eros
              </td>
            </tr>
            <tr>
              <td>大</td>
              <td>遊戲進入每一課。</td>
              <td>
                Mauris non tempor quam, et lacinia sapien
                auris accumsan eros
              </td>
            </tr>
            <tr>
              <td>大</td>
              <td>遊戲進入每一課。</td>
              <td>
                Mauris non tempor quam, et lacinia sapien
                auris accumsan eros
              </td>
            </tr>
            <tr>
              <td>大</td>
              <td>遊戲進入每一課。</td>
              <td>
                Mauris non tempor quam, et lacinia sapien
                auris accumsan eros
              </td>
            </tr>
          </table>
          <div class="row">
            <div class="col-md-3">
              <a href="home.html"><p class="gray-btn">Home page</p></a>
            </div>
            <div class="col-md-3 col-md-offset-6 text-right">
              <div class="btn btn-green">Next Review</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Card from '../components/Card.vue'
export default {
  name: 'me',
  data () {
    return {
      initialFetchComplete: false,
      msg: 'The route works',
      reviewDeck: [],
      errors: null
    }
  },
  components: {
    'card': Card
  },
  created () {
    this.getReviewDeck()
  },
  methods: {
    getReviewDeck () {
      var level = this.$route.params.lvl
      var sublevel = this.$route.params.sublevel
      var url = '/api/review/lvl-' + level + '/' + sublevel + '/get'
      this.$http.get(url)
        .then(response => {
          this.errors = null
          this.reviewDeck = response.data
          this.initialFetchComplete = true
 /* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
        this.initialFetchComplete = true
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
</style>
