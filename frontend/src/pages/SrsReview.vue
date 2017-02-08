<template>
<div class="internal-page">
  <div class="top-progress">
    <div class="top-progress__inner" style="width: 76%"></div>
  </div>

  <div class="green-cover green-cover__full-page">
    <div class="row green-cover__head">
      <div class="col-md-2 col-sm-1">
        <router-link to="/dashboard">
          <div class="logo">
            <img src="../assets/img/logo-white.svg" alt="">
          </div>
        </router-link>
        <transition name="modal">
          <completeModal v-show="showCompleteModal" @close="showCompleteModal = false">
            <span slot="header">
              Good Job! 
            </span>
            <span slot="body">
              Great job getting your reviews down to 0! Just remember to check back often so they don't pile up!
            </span>
            <div slot="footer">
              <router-link to="/dashboard">
                <div class="btn btn-green">Dashboard</div>
              </router>
            </div>
          </completeModal>
        </transition>
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
import baseModal from '../components/modalBase.vue'
export default {
  name: 'srsreview',
  data () {
    return {
      initialFetchComplete: false,
      reviewWords: [],
      currentWord: '',
      wordsComplete: '',
      showCompleteModal: false
    }
  },
  components: {
    'card': Card,
    'counterRatio': counterRatio,
    'completeModal': baseModal
  },
  created () {
    this.getReviewDeck()
    window.eventHub.$on('completeCard', this.completeCard)
    window.eventHub.$on('deckComplete', this.deckComplete)
  },
  beforeDestroy () {
    window.eventHub.$off('completeCard', this.completeCard)
    window.eventHub.$on('deckComplete', this.deckComplete)
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
      }, error => {
        if (error) {
          this.errors = 'Could not fetch deck from server!'
          this.initialFetchComplete = true
        }
      })
    },
    completeCard: function (arrayIndex, bothCorrect) {
      var url = '/api/review/update-word'
      var thisWordID = this.reviewWords[arrayIndex].id
      var increase = bothCorrect ? 1 : 0
      if (bothCorrect) {
        window.eventHub.$emit('increment')
      } else {
        if (this.reviewWords.length - this.array_index > 7) {
          this.reviewWords.splice(this.arrayIndex + 7, 0, this.reviewWords[arrayIndex])
        } else {
          this.reviewWords.push(this.reviewWords[arrayIndex])
        }
      }
      this.$http.post(url, {'known_word_id': thisWordID, 'increase_level': increase}, {headers: auth.getAuthHeader()})
      .then(response => {
      }, error => {
        if (error) {
          this.errors = 'Could not update on server!'
        }
      })
    },
    deckComplete: function () {
      this.showCompleteModal = true
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
