<template>
<div class="internal-page">
  <div class="top-progress">
    <div class="top-progress__inner" style="width: 76%"></div>
  </div>

  <div class="green-cover green-cover__srs-review">
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
    window.eventHub.$on('completeCard', this.completeCard)
  },
  beforeDestroy () {
    window.eventHub.$off('completeCard', this.completeCard)
  },
  methods: {
    getReviewDeck: function () {
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
    },
    completeCard: function (array_index, bothCorrect) {
      var url = '/api/review/update-word'
      var thisWordID = this.reviewWords[array_index].id
      var increase = bothCorrect ? 1 : 0
      if (bothCorrect) {
        window.eventHub.$emit('increment')
      } else {
        if (this.reviewWords.length - this.array_index > 7) {
          this.reviewWords.splice(this.array_index + 7, 0, this.reviewWords[array_index])
        } else {
          this.reviewWords.push(this.reviewWords[array_index])
        }
      }
      this.$http.post(url, {'known_word_id': thisWordID, 'increase_level': increase}, {headers: auth.getAuthHeader()})
      .then(response => {
      }, error => {
        if (error) {
          this.errors = 'Could not update on server!'
        }
      })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
