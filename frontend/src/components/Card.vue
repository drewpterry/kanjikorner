<template>
<div>
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
      <input v-on:keyup.enter="submitAnswer" id="answer-input" type="text" class="c-textarea" title="your answer" placeholder="よみ" focus>
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
import auth from '../auth'
import wanakana from 'wanakana/lib/wanakana.min.js'
export default {
  name: 'Card',
  data () {
    return {
      initialFetchComplete: false,
      show: true,
      wordList: this.words,
      leaveClass: '',
      currentWord: '',
      currentIndex: 0,
      currentMeanings: [],
      front: '',
      back: '',
      answer_type: 'reading',
      bothAnswerCorrect: true,
      inputIME: '',
      enterAllowed: true
    }
  },
  props: {
    'words': {
      type: Array,
      required: true
    },
    'deck': {
      type: Boolean
    }
  },
  created () {
    this.currentIndex = 0
    this.setCurrentWord()
    this.front = this.currentWord.real_word
    this.back = this.currentWord.hiragana
    this.setMeanings()
  },
  mounted () {
    this.inputIME = document.getElementById('answer-input')
    wanakana.bind(this.inputIME)
  },
  methods: {
    setCurrentWord: function () {
      if (this.deck) {
        this.currentWord = this.wordList[0].words[this.currentIndex]
      } else {
        this.currentWord = this.wordList[this.currentIndex].words
      }
    },
    setMeanings: function () {
      this.currentMeanings = []
      var self = this
      this.currentWord.meanings.forEach(function (el, i) {
        self.currentMeanings.push(el.meaning)
      })
    },
    flipCard: function () {
      document.getElementById('card').classList.toggle('flip')
    },
    nextCard: function (correct) {
      this.leaveClass = correct ? 'animated bounceOutRight' : 'animated bounceOutLeft'
      this.$nextTick(function () {
        this.show = false
      })
      this.currentIndex = this.currentIndex + 1
      this.setCurrentWord()
      this.front = this.currentWord.real_word
      this.back = this.currentWord.hiragana
      this.$nextTick(function () {
        this.setMeanings()
      })
      setTimeout(this.showNewCard, 400)
    },
    showNewCard: function () {
      this.show = true
    },
    submitAnswer: function () {
      var self = this
      if (this.enterAllowed === false) {
        return
      }
      this.enterAllowed = false
      if (this.checkAnswer()) {
        if (this.answer_type === 'reading') {
          console.log('correct and reading')
        } else {
          // consider making nextCard time as being an argument
          self.nextCard(true)
          console.log('correct and meanings')
        }
        setTimeout(function () {
          self.enterAllowed = true
          self.setAnswerType()
        }, 1000)
      } else {
        this.bothAnswerCorrect = false
        self.flipCard()
        setTimeout(function () {
          self.flipCard()
          self.enterAllowed = true
          self.setAnswerType()
        }, 2000)
        if (this.answer_type === 'reading') {
          console.log('wrong and reading')
        } else {
          setTimeout(function () {
            self.nextCard(true)
          }, 2500)
          console.log('wrong and meaning')
        }
      }
      // determine what to do if both meaning and reading have been answered
      if (this.answer_type === 'meaning') {
        this.postAnswerResult()
        // reset to default state
        this.bothAnswerCorrect = true
      }
    },
    postAnswerResult: function () {
      var url = '/api/review/update-word'
      var thisWordID = this.wordList[this.currentIndex].id
      if (this.bothAnswerCorrect) {
        this.$http.post(url, {'known_word_id': thisWordID, 'increase_level': '1'}, {headers: auth.getAuthHeader()})
        .then(response => {
        }, error => {
          if (error) {
            this.errors = 'Could not update on server!'
          }
        })
      } else {
        console.log('got here')
        this.$http.post(url, {'known_word_id': thisWordID, 'increase_level': '0'}, {headers: auth.getAuthHeader()})
        .then(response => {
        }, error => {
          if (error) {
            this.errors = 'Could not update on server!'
          }
        })
        if (this.wordList.length - this.currentIndex > 7) {
          this.wordList.splice(this.currentIndex + 7, 0, this.wordList[this.currentIndex])
        } else {
          this.wordList.push(this.wordList[this.currentIndex])
        };
      }
    },
    setIME: function () {
      this.inputIME.value = ''
      if (this.answer_type === 'reading') {
        wanakana.bind(this.inputIME)
        this.inputIME.placeholder = 'よみ'
      } else {
        wanakana.unbind(this.inputIME)
        this.inputIME.placeholder = 'meaning'
      }
    },
    setAnswerType: function () {
      this.answer_type = this.answer_type === 'reading' ? 'meaning' : 'reading'
      this.setIME()
      if (this.answer_type === 'meaning') {
        this.back = this.setDefinitionFormat()
      }
    },
    checkAnswer: function () {
      if (this.answer_type === 'reading') {
        if (this.inputIME.value === this.back) {
          return true
        } else {
          return false
        }
      } else {
        return this.checkDefinitions()
      }
    },
    checkDefinitions: function () {
      var self = this
      var answerCorrect = false
      var submittedAnswer = this.inputIME.value
      // consider using normal for iterator so that you can use break statement
      this.currentMeanings.forEach(function (def, i) {
        var lettersOff = self.getLevenshtein(submittedAnswer, def)
        var percentIncorrect = lettersOff / def.length
        if (percentIncorrect < 0.33) {
          answerCorrect = true
        }
      })
      return answerCorrect
    },
    setDefinitionFormat: function () {
      var defString = ''
      this.currentMeanings.forEach(function (def, i) {
        defString += def + ','
      })
      return defString
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
  transition: 0.4s;
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
