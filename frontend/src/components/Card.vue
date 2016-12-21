<template>
<div>
  
  <div id="example-3">
    <button @click="nextCard(true)">
      Toggle render
    </button>
    <button @click="nextCard(false)">
      Toggle left 
    </button>
    <button @click="flipCard">
      flip 
    </button>
  </div>
    <div id="card" class="flip-container">
      <transition
        name="custom-classes-transition"
        enter-active-class="animated fadeIn"
        v-bind:leave-active-class="leaveClass"
      >
        <div v-if="show" class="flipper">
          <div class="front panel panel-task">
            {{ front }} 
          </div>
          <div class="back panel panel-task">
            {{ back }} 
          </div>
        </div>
      </transition>
    </div>
    <div class="panel panel-answer">
      <input v-on:keyup.enter="submitAnswer" id="answer-input" type="text" class="c-textarea" title="your answer" value="ひらがな">
      <div class="row">
        <div class="col-md-3">
          <p class="gray-btn">I don't know</p>
        </div>
        <div class="col-md-3 col-md-offset-6 text-right">
          <div class="btn btn-red">Next</div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
import wanakana from 'wanakana/lib/wanakana.min.js'
export default {
  name: 'Card',
  data () {
    return {
      initialFetchComplete: false,
      show: true,
      leaveClass: '',
      currentWord: '',
      currentIndex: 0,
      front: '',
      back: '',
      answer_type: 'reading',
      inputIME: '',
      enterAllowed: true
    }
  },
  props: ['words'],
  created () {
    this.currentWord = this.words[0]
    this.front = this.currentWord.words.real_word
    this.back = this.currentWord.words.hiragana
  },
  mounted () {
    this.inputIME = document.getElementById('answer-input')
    wanakana.bind(this.inputIME)
  },
  methods: {
    flipCard: function flipCard () {
      document.getElementById('card').classList.toggle('flip')
    },
    nextCard: function (correct) {
      this.leaveClass = correct ? 'animated bounceOutRight' : 'animated bounceOutLeft'
      this.$nextTick(function () {
        this.show = false
      })
      this.currentIndex = this.currentIndex + 1
      this.currentWord = this.words[this.currentIndex]
      this.front = this.currentWord.words.real_word
      this.back = this.currentWord.words.hiragana
      setTimeout(this.showNewCard, 400)
    },
    showNewCard: function () {
      this.show = true
    },
    submitAnswer: function () {
      if (this.enterAllowed === false) {
        return
      }
      this.checkAnswer()
      var self = this
      this.enterAllowed = false
      this.flipCard()
      setTimeout(function () {
        self.flipCard()
        self.enterAllowed = true
      }, 2000)
      if (this.answer_type === 'meaning') {
        setTimeout(function () {
          self.nextCard(true)
        }, 3000)
      }
      this.setAnswerType()
      this.setIME()
    },
    setIME: function () {
      if (this.answer_type === 'reading') {
        wanakana.bind(this.inputIME)
      } else {
        wanakana.unbind(this.inputIME)
      }
    },
    setAnswerType: function () {
      this.answer_type = this.answer_type === 'reading' ? 'meaning' : 'reading'
    },
    checkAnswer: function () {
      console.log(this.getLevenshtein('hello', 'hell'))
      if (this.inputIME.value === this.back) {
        console.log(true)
        return true
      } else {
        console.log(false)
        return false
      }
    },
    getLevenshtein: function (a, b) {
      function levenshteinenator (a, b) {
        var cost
        var m = a.length
        var n = b.length

        // make sure a.length >= b.length to use O(min(n,m)) space
        if (m < n) {
          var c = a; a = b; b = c
          var o = m; m = n; n = o
        }

        var r = []; r[0] = []
        for (c = 0; c < n + 1; ++c) {
          r[0][c] = c
        }

        for (var i = 1; i < m + 1; ++i) {
          r[i] = []; r[i][0] = i
          for (var j = 1; j < n + 1; ++j) {
            cost = a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1
            r[i][j] = minimator(r[i - 1][j] + 1, r[i][j - 1] + 1, r[i - 1][j - 1] + cost)
          }
        }

        return r[r.length - 1][r[r.length - 1].length - 1]
      }

      /**
       * Return the smallest of the three numbers passed in
       * @param Number x
       * @param Number y
       * @param Number z
       * @return Number
       */
      function minimator (x, y, z) {
        if (x < y && x < z) return x
        if (y < x && y < z) return y
        return z
      }

      return levenshteinenator(a, b)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .flip-container {
    margin-bottom: 5px;
    perspective: 1000px;
  }
  /* flip the pane when hovered */
  .flip .flipper, {
    transform: rotateY(180deg);
  }

.flip-container, .front, .back {
  width: 610px;
  height: 300px;
}

/* flip speed goes here */
.flipper {
  transition: 0.6s;
  transform-style: preserve-3d;
  position: relative;
}

/* hide back of pane during swap */
.front, .back {
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
}

/* front pane, placed above back */
.front {
  z-index: 2;
  /* for firefox 31 */
  transform: rotateY(0deg);
}

/* back, initially hidden pane */
.back {
  transform: rotateY(180deg);
}
</style>
