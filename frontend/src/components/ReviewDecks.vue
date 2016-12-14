<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Level {{ $route.params.lvl }} </h2>
    <h2>{{ currentWord.real_word }}</h2>
    <tbody>
      <!--<tr v-for="word in reviewDeck.words">-->
        <td></td>
      <!--</tr>-->
    </tbody>
  </div>
</template>

<script>
export default {
  name: 'me',
  data () {
    return {
      initialFetchComplete: false,
      msg: 'The route works',
      reviewDeck: [],
      currentWord: '',
      errors: null
    }
  },
  // props: ['companyId'],
  created () {
    this.getReviewDeck()
  },
  methods: {
    getReviewDeck () {
      var level = this.$route.params.lvl
      var sublevel = this.$route.params.sublevel
      var url = '/api/review/lvl-' + level + '/' + sublevel + '/get'
      // var url = '/api/all-decks'
      this.$http.get(url)
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data[0]
        this.initialFetchComplete = true
        this.currentWord = this.reviewDeck.words[0]
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
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
