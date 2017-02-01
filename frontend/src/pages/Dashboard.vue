<template>
<div class="internal-page">
  <div class="top-line">
    <div class="container">
      <div class="col-md-5 col-md-offset-7">
        <ul class="main-nav">
          <li><a href="">About</a></li>
          <li><a href="">FAQ</a></li>
          <li><a href="">Guide</a></li>
          <li><span v-on:click="logout">Logout</span></li>
          <li class="social"><a href=""><i class="icon icon-tw"></i></a></li>
          <li class="social"><a href=""><i class="icon icon-fb"></i></a></li>
        </ul>
      </div>
    </div>
  </div>
 
  <div class="header">
    <div class="container">
      <div class="col-md-2">
        <div class="logo">
          <img src="../assets/img/logo.svg" alt="">
        </div>
      </div>
      <div class="col-md-2 col-md-offset-6">
        <router-link to="/review/srs">
          <button v-if="isNaN(reviewData.next_review)" disabled class="btn btn-red">Reviews: 0 </button>
          <button v-else class="btn btn-red">Reviews: {{ reviewData.next_review }} </button>
        </router-link>
      </div>
      <div class="col-md-2">
        <div class="user-dropdown">
          <div class="user-dropdown__img">
            <img src="../assets/img/content/user@2x.png" class="img-responsive" alt="">
          </div>
          <span class="user-dropdown__name">
            Andrew
          </span>
        </div>
      </div>
    </div>
  </div>
 
  <div class="graph">
    <div class="container">
      <div class="col-md-2 graph__side">
        <div class="panel">
          <p class="panel__title">{{ reviewData.next_review }}</p>
          <p class="panel__text">Reviews Due Now</p>
        </div>
        <div class="panel">
          <p class="panel__title">{{ reviewData.next_day }}</p>
          <p class="panel__text">Due Next 24 Hrs</p>
        </div>
        <p class="dark-title">NEW WORDS ADDED</p>
        <div class="panel panel-double">
          <div class="panel-double__left">
            <p class="panel__title">15</p>
            <p class="panel__text">Today</p>
          </div>
          <div class="panel-double__right">
            <p class="panel__title">21</p>
            <p class="panel__text">Daily Goal</p>
          </div>
        </div>
        <p class="dark-title">WORDS REVIEWED</p>
        <div class="panel panel-double">
          <div class="panel-double__left">
            <p class="panel__title">{{ userProfile.number_words_practiced_today }}</p>
            <p class="panel__text">Today</p>
          </div>
          <div class="panel-double__right">
            <p class="panel__title">1124</p>
            <p class="panel__text">This Week</p>
          </div>
        </div>
      </div>
      <div class="col-md-8 graph__wrap">
        <img src="../assets/img/content/graph.png" class="img-responsive" alt="">
      </div>
      <div class="col-md-2 graph__side">
        <div class="panel">
          <div class="graph-stat">
            <p class="graph-stat__text">Words reviewed</p>
            <p class="graph-stat__number">{{ userProfile.total_reviews_ever }}</p>
          </div>
          <div class="graph-stat">
            <p class="graph-stat__text">Words reviewed correct</p>
            <p class="graph-stat__number">{{ userProfile.percent_correct }}<sup>%</sup></p>
          </div>
          <div class="graph-stat">
            <p class="graph-stat__text">Words reviewed</p>
            <p class="graph-stat__number">11124</p>
          </div>
          <div class="graph-stat">
            <p class="graph-stat__text">Words reviewed correct</p>
            <p class="graph-stat__number">86<sup>%</sup></p>
          </div>
        </div>
      </div>
    </div>
  </div>
 
  <div class="stuff">
    <div class="container">
      <div v-if="initialFetchComplete" class="panel stuff-head">
        <div v-for="n in 10" class="stuff-head-item">
          <p class="stuff-head-item__title">{{ wordLevelNames[n-1] }}</p>
          <p class="stuff-head-item__number">{{ reviewData.tier_counts[n-1] }}</p>
        </div>
      </div>
      <div class="level" v-for="level in reviewDeckLevels">
        <div class="row">
          <div class="col-md-2">
            <p class="level__title"><span>{{ level }}</span> Level</p>
          </div>
          <div class="col-md-10">
            <p class="level__lessons-number">20 lessons</p>
            <div class="level__progress">
              <div class="level__progress-inner" style="width: 90%"></div>
            </div>
          </div>
        </div>
        <div class="level__wrap">
          <div class="level-slider js-level-slider">
            <div v-for="number in 20">
              <div class="level-slider__slide">
                <router-link :to="{ name: 'deck', params: { lvl:level, sublevel:number } }">
                  <div class="panel lesson-panel checked">
                    <p class="lesson-panel__number">{{ number }} lesson</p>
                    <p class="lesson-panel__words">20 words</p>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="level" v-for="level in reviewDeckLevels">
        <div class="row">
          <div class="col-md-2">
            <p class="level__title"><span>{{ level }}</span> Level</p>
          </div>
          <div class="col-md-10">
            <p class="level__lessons-number">20 lessons</p>
            <div class="level__progress">
              <div class="level__progress-inner" style="width: 90%"></div>
            </div>
          </div>
        </div>
        <div class="level__wrap">
          <div class="level-slider js-level-slider">
            <div v-for="number in 20">
              <div class="level-slider__slide">
                <router-link :to="{ name: 'deck', params: { lvl:level, sublevel:number } }">
                  <div class="panel lesson-panel checked">
                    <p class="lesson-panel__number">{{ number }} lesson</p>
                    <p class="lesson-panel__words">20 words</p>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

 <div class="footer">
   <div class="container">
     <div class="col-md-7">
       <p class="copyright">Copyright 2016. Kanjisama.com. All roghts reserved.</p>
     </div>
     <div class="col-md-5">
       <ul class="main-nav">
         <li><a href="">About</a></li>
         <li><a href="">FAQ</a></li>
         <li><a href="">Guide</a></li>
         <li class="social"><a href=""><i class="icon icon-tw"></i></a></li>
         <li class="social"><a href=""><i class="icon icon-fb"></i></a></li>
       </ul>
     </div>
   </div>
 </div>
</div>
</template>

<script>
import auth from '../auth'
export default {
  name: 'DASBOARD',
  data () {
    return {
      msg: 'The route works',
      initialFetchComplete: false,
      reviewDeck: [],
      reviewDeckLevels: 0,
      userProfile: [],
      reviewData: [],
      wordLevelNames: ['ゼロ', '一', '二', '三', '四', '五', '六', '七', '八', 'パス'],
      errors: null
    }
  },
  created () {
    this.getReviewDeck()
    this.getUserProfile()
    this.getReviewData()
    // hack - this inserts jquery and slick carousel into this page for carousel animation - ideally this should be a carousel component
    var elTow = document.createElement('script')
    elTow.setAttribute('type', 'text/javascript')
    elTow.setAttribute('src', 'https://code.jquery.com/jquery-2.2.4.min.js')
    document.getElementsByTagName('head')[0].appendChild(elTow)
    setTimeout(function () {
      var el = document.createElement('script')
      el.setAttribute('type', 'text/javascript')
      el.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.js')
      document.getElementsByTagName('head')[0].appendChild(el)
    }, 1000)
  },
  methods: {
    setSlick () {
/* eslint-disable */
      $(document).ready(function () {
        $('.js-level-slider').slick({
          infinite: false,
          slidesToShow: 5,
          slidesToScroll: 5,
          responsive: [
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 3,
                slidesToScroll:3
              }
            },
            {
              breakpoint: 420,
              settings: {
                slidesToShow: 2,
                slidesToScroll:2
              }
            }
          ]
        })
      })
    },
    getReviewDeck () {
      // var url = '/api/all-decks/get'
      var url = '/api/user-decks/get'
      this.$http.get(url, {headers: auth.getAuthHeader()})
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data
        this.reviewDeckLevels = this.reviewDeck[this.reviewDeck.length - 1].sets_fk.level
        console.log(this.reviewDeck.length)
        var self = this
        setTimeout(function () {
          self.setSlick()
        }, 2000)
/* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
      })
    },
    getUserProfile () {
      var url = '/api/profile-data/get'
      this.$http.get(url, {headers: auth.getAuthHeader()})
      .then(response => {
        this.errors = null
        this.userProfile  = response.data
/* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
      })
    },
    getReviewData () {
      var url = '/api/review-data/get'
      this.$http.get(url, {headers: auth.getAuthHeader()})
      .then(response => {
        this.errors = null
        this.reviewData = response.data
        this.initialFetchComplete = true
/* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
      })
    },
    logout: function () {
      auth.logout()
    }
  },
  route: {
    // Check the users auth status before
    // allowing navigation to the route
    canActivate() {
      return auth.user.authenticated
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
</style>
