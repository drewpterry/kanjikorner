<template>
<div>
  <div id="card" class="flip-container" v-on:click="flip_card">
    <div class="flipper">
      <div class="front panel panel-task">
        front
      </div>
      <div class="back panel panel-task">
        back
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
      msg: 'SRS REview'
    }
  },
  methods: {
    flip_card () {
      document.getElementById('card').classList.toggle('flip')
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
