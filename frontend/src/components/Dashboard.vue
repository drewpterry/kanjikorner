<template>
<div>

  <div class="top-line">
    <div class="container">
      <div class="col-md-5 col-md-offset-7">
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
 
  <div class="header">
    <div class="container">
      <div class="col-md-2">
        <div class="logo">
          <img src="../assets/img/logo.svg" alt="">
        </div>
      </div>
      <div class="col-md-2 col-md-offset-6">
        <router-link to="/review/srs">
          <button class="btn btn-red">Reviews: 11224</button>
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
          <p class="panel__title">1124</p>
          <p class="panel__text">Reviews Due Now</p>
        </div>
        <div class="panel">
          <p class="panel__title">1124</p>
          <p class="panel__text">Reviews Due Now</p>
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
            <p class="panel__title">211</p>
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
            <p class="graph-stat__number">11124</p>
          </div>
          <div class="graph-stat">
            <p class="graph-stat__text">Words reviewed correct</p>
            <p class="graph-stat__number">86<sup>%</sup></p>
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
      <div class="panel stuff-head">
 
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">ゼロ</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">一</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">二</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">三</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">四</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">五</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">六</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">七</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">八</p>
          <p class="stuff-head-item__number">2134</p>
        </div>
        <div class="stuff-head-item">
          <p class="stuff-head-item__title">パス</p>
          <p class="stuff-head-item__number">2134</p>
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


<!--<script src="js/lib/jquery-2.2.4.min.js"></script>-->
<!--<script src="js/lib/bootstrap.min.js"></script>-->
<!--<script src="js/lib/slick.min.js"></script>-->
<!--<script src="js/main.js"></script>-->

</div>
</template>

<script>
export default {
  name: 'DASBOARD',
  data () {
    return {
      initialFetchComplete: false,
      msg: 'The route works',
      reviewDeck: [],
      reviewDeckLevels: 0,
      errors: null
    }
  },
  created () {
    this.getReviewDeck()
  },
  methods: {
    getReviewDeck () {
      var url = '/api/all-decks'
      this.$http.get(url)
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data
        this.reviewDeckLevels = this.reviewDeck[this.reviewDeck.length - 1].level
        console.log(this.reviewDeckLevels)
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
<style lang="scss">
</style>
