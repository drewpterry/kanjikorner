<template>
<div class="internal-page">
  <div class="top-progress">
    <div class="top-progress__inner" style="width: 76%"></div>
  </div>

  <div class="green-cover">
    <div class="row green-cover__head">
      <div class="col-md-2 col-sm-1">
        <router-link to="/dashboard">
          <div class="logo">
            <img src="../assets/img/logo-white.svg" alt="">
          </div>
        </router-link>
      </div>
      <div class="col-md-offset-9 col-md-1">
        <p class="green-cover__progress">2 / {{ reviewWords.length }}</p>
      </div>
    </div>
    <div class="container green-cover__body">
      <div class="row ">
        <div class="col-md-offset-2 col-md-8">
          <card v-if="initialFetchComplete" v-bind:words="reviewWords"></card>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import auth from '../auth'
import Card from '../components/Card.vue'
export default {
  name: 'srsreview',
  data () {
    return {
      initialFetchComplete: false,
      msg: 'SRS REview',
      reviewWords: [],
      currentWord: ''
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
      var url = '/api/review/srs/get'
      this.$http.get(url, {headers: auth.getAuthHeader()})
      .then(response => {
        this.errors = null
        this.reviewWords = response.data
        this.initialFetchComplete = true
        this.currentWord = this.reviewWords.words
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
<style scoped>
</style>
