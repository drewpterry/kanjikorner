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
    <div class="panel input-panel">
      <input v-on:keyup.enter="submitAnswer" id="answer-input" type="text" class="c-textarea" title="your answer" placeholder="よみ" focus>
      <span v-if="answerStatus == 'correct'"  id="maru" class="answer-notifier">o</span>
      <span v-if="answerStatus == 'incorrect'" id="batsu" class="answer-notifier">x</span>
    </div>
</div>
</template>

<script>
import wanakana from 'wanakana/lib/wanakana.min.js'
import helper from '../helpers'
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
      answerStatus: '',
      inputIME: '',
      enterAllowed: true
    }
  },
  props: {
    'words': {
      required: true
    },
    'deck': {
      type: Boolean
    }
  },
  created () {
    this.setInitialState()
    window.eventHub.$on('reset', this.resetInitialState)
  },
  mounted () {
    this.inputIME = document.getElementById('answer-input')
    wanakana.bind(this.inputIME)
  },
  methods: {
    setInitialState: function () {
      this.currentIndex = 0
      if (this.deck) {
        this.wordList = this.words.words
      } else {
        this.wordList = this.words
      }
      this.setCurrentWord(this.currentIndex)
      this.front = this.currentWord.real_word
      this.back = this.currentWord.hiragana
      this.$nextTick(function () {
        this.setMeanings()
      })
    },
    resetInitialState: function () {
      this.setInitialState()
      setTimeout(this.showNewCard, 400)
    },
    setCurrentWord: function (currentIndex) {
      if (this.deck) {
        this.currentWord = this.wordList[currentIndex]
      } else {
        this.currentWord = this.wordList[currentIndex].words
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
      if (this.wordList.length !== this.currentIndex) {
        var self = this
        this.setCurrentWord(this.currentIndex)
        setTimeout(function () {
          self.front = self.currentWord.real_word
          self.back = self.currentWord.hiragana
          self.$nextTick(function () {
            self.setMeanings()
          })
          self.showNewCard()
        }, 400)
      } else {
        console.log('complete')
        window.eventHub.$emit('deckComplete')
      }
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
        this.answerStatus = 'correct'
        if (this.answer_type === 'reading') {
          console.log('correct and reading')
        } else {
          window.eventHub.$emit('completeCard', this.currentIndex, this.bothAnswerCorrect)
          // consider making nextCard time as being an argument
          self.nextCard(this.bothAnswerCorrect)
          console.log('correct and meanings')
        }
        setTimeout(function () {
          self.answerStatus = ''
          self.enterAllowed = true
          self.setAnswerType()
        }, 1000)
      } else {
        this.answerStatus = 'incorrect'
        this.bothAnswerCorrect = false
        self.flipCard()
        setTimeout(function () {
          self.answerStatus = ''
          self.flipCard()
          self.enterAllowed = true
          self.setAnswerType()
        }, 2000)
        if (this.answer_type === 'reading') {
          console.log('wrong and reading')
        } else {
          window.eventHub.$emit('completeCard', this.currentIndex, this.bothAnswerCorrect)
          setTimeout(function () {
            self.nextCard(this.bothAnswerCorrect)
          }, 2500)
          console.log('wrong and meaning')
        }
      }
      // determine what to do if both meaning and reading have been answered
      if (this.answer_type === 'meaning') {
        // reset to default state
        this.bothAnswerCorrect = true
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
      var self = this
      if (this.answer_type === 'meaning') {
        setTimeout(function () {
          self.back = helper.arrayToCommaSeperatedString(self.currentMeanings)
        }, 400)
      }
    },
    checkAnswer: function () {
      if (this.answer_type === 'reading') {
        return this.inputIME.value === this.back
      } else {
        return this.checkDefinitions()
      }
    },
    checkDefinitions: function () {
      var answerCorrect = false
      var submittedAnswer = this.inputIME.value
      // consider using normal for iterator so that you can use break statement
      this.currentMeanings.forEach(function (def, i) {
        var lettersOff = helper.getLevenshtein(submittedAnswer, def)
        var percentIncorrect = lettersOff / def.length
        if (percentIncorrect < 0.33) {
          answerCorrect = true
        }
      })
      return answerCorrect
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "~assets/style/_vars.scss";
  #answer-input {
   text-align: center; 
   font-size: 1.5em;
  }

  .flip-container {
    margin-bottom: 5px;
    perspective: 1000px;
  }
  /* flip the pane when hovered */
  .flip .flipper, {
    transform: rotateY(180deg);
  }

.flip-container, .front, .back {
  width: 100%;
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

.input-panel {
  position:relative;
}

.answer-notifier {
  position: absolute;
  top: 10%;
  right: 4%;
  font-size: 3em;
}

#maru {
  color: $main-green;
}

#batsu {
  color: $tomato;
}
</style>
