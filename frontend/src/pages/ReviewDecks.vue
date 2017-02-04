<template>
<div class="internal-page">
  <div class="green-cover">
    <div class="row green-cover__head">
      <div class="col-md-2 col-sm-1">
        <router-link to="/dashboard">
          <div class="logo">
            <img src="../assets/img/logo-white.svg" alt="">
          </div>
        </router-link>
      </div>
      <counterRatio v-if="initialFetchComplete" :initialDenominator="reviewDeck[0].words.length"></counterRatio>
    </div>
    <transition name="modal">
      <modal v-show="showModal" @close="showModal= false">
      </modal>
    </transition>
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
            <p class="simple-text">{{ currentWord.hiragana }}</p>
          </div>
        </div>
        <div class="row lesson__row">
          <div class="col-md-3">
            <p class="gray-title">POS:</p>
          </div>
          <div v-for="pos in currentWord.pos" class="col-md-2">
            <p class="simple-text">{{ pos.pos }}, </p>
          </div>
        </div>
        <div class="row lesson__row">
          <div class="col-md-3">
            <p class="gray-title">Kanji:</p>
          </div>
          <div v-for="kanji in currentWord.kanji" class="col-md-3">
            <div class="panel text-center">
              {{ kanji }} 
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
</template>

<script>
import auth from '../auth'
import Card from '../components/Card.vue'
import counterRatio from '../components/counterRatio.vue'
import completeModal from '../components/deckReviewCompleteModal.vue'
export default {
  name: 'me',
  data () {
    return {
      initialFetchComplete: false,
      deckId: '',
      msg: 'The route works',
      reviewDeck: [],
      reviewDeckOriginal: [],
      currentCardIndex: 0,
      currentWord: '',
      secondReview: false,
      showModal: false,
      errors: null
    }
  },
  components: {
    'card': Card,
    'counterRatio': counterRatio,
    'modal': completeModal
  },
  created () {
    this.getReviewDeck()
    window.eventHub.$on('completeCard', this.completeCard)
    window.eventHub.$on('deckComplete', this.deckComplete)
  },
  beforeDestroy () {
    window.eventHub.$off('completeCard', this.completeCard)
    window.eventHub.$off('deckComplete', this.deckComplete)
  },
  methods: {
    getReviewDeck () {
      var level = this.$route.params.lvl
      var sublevel = this.$route.params.sublevel
      var url = '/api/review/lvl-' + level + '/' + sublevel + '/get'
      this.$http.get(url, {headers: auth.getAuthHeader()})
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data
        this.reviewDeckOriginal = response.data
        this.deckId = response.data[0].id
        this.setCurrentWord()
        this.initialFetchComplete = true
 /* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
        this.initialFetchComplete = true
      })
    },
    completeCard: function (array_index, bothCorrect) {
      this.currentCardIndex++
      this.setCurrentWord()
      if (bothCorrect) {
        window.eventHub.$emit('increment')
      } else {
        this.reviewDeck[0].words.push(this.reviewDeck[0].words[array_index])
      }
    },
    postStackComplete () {
      var url = '/api/review/review-deck-complete'
      this.$http.post(url, {'stack_id': this.deckId}, {headers: auth.getAuthHeader()})
      .then(response => {
        this.showModal = true
      }, error => {
        if (error) {
          this.errors = 'Oh no! Something went wrong and we couldn\t save your wordsi!'
        }
      })
    },
    deckComplete: function () {
      if (this.secondReview) {
        this.postStackComplete()
      } else {
        window.eventHub.$emit('reset')
        this.currentCardIndex = 0
        this.setCurrentWord()
        this.reviewDeck = this.reviewDeckOriginal
        this.secondReview = true
      }
    },
    setCurrentWord: function () {
      this.currentWord = this.reviewDeck[0].words[this.currentCardIndex]
      console.log(this.currentWord)
      console.log(this.currentCardIndex)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
</style>
