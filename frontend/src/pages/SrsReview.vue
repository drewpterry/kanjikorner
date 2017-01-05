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
      <counterRatio v-if="initialFetchComplete" :initialDenominator="reviewWords.length"></counterRatio>
    </div>
    <div class="container green-cover__body">
      <div class="row ">
        <div class="col-md-offset-2 col-md-8">
          <card v-if="initialFetchComplete" :words="reviewWords"></card>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import auth from '../auth'
import Card from '../components/Card.vue'
import counterRatio from '../components/counterRatio.vue'
export default {
  name: 'srsreview',
  data () {
    return {
      initialFetchComplete: false,
      reviewWords: [],
      currentWord: '',
      wordsComplete: ''
    }
  },
  components: {
    'card': Card,
    'counterRatio': counterRatio
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
