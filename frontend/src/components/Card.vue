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
      <input v-on:keyup.enter="submitAnswer" type="text" class="c-textarea" title="your answer" cols="30" rows="5">
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
      answer_type: 'reading'
    }
  },
  props: ['words'],
  created () {
    this.currentWord = this.words[0]
    this.front = this.currentWord.words.real_word
    this.back = this.currentWord.words.hiragana
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
      this.flipCard()
      setTimeout(this.flipCard, 2000)
      if (this.answer_type === 'meaning') {
        var self = this
        setTimeout(function () {
          self.nextCard(true)
        }, 3000)
      }
      this.setAnswerType()
    },
    setAnswerType: function () {
      this.answer_type = this.answer_type === 'reading' ? 'meaning' : 'reading'
    },
    checkAnswer: function () {
      this.flipCard()
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
