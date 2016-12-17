<template>
<div>
      <div class="col-md-2 col-md-offset-6">
        <router-link to="/dashboard">
          <button class="btn btn-red">Reviews: 11224</button>
        </router-link>
      </div>
</div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      reviewDeck: [],
      errors: null
    }
  },
  created () {
    this.getReviewDeck()
  },
  methods: {
    getReviewDeck () {
      var url = '/api/all-decks/get'
      this.$http.get(url)
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data
        this.reviewDeckLevels = this.reviewDeck[this.reviewDeck.length - 1].level
/* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
</style>
