<template>
<div>
    <div class="col-md-offset-8 col-md-2">
      <p class="green-cover__progress">{{ numerator }} / {{ denominator }}</p>
    </div>
</div>
</template>

<script>
export default {
  name: 'counterRatio',
  data () {
    return {
      denominator: '',
      numerator: 0
    }
  },
  props: {
    'initialDenominator': {
      type: Number,
      required: true
    },
    'initialNumerator': {
      type: Number
    }
  },
  created () {
    this.denominator = this.initialDenominator
    this.numberator = this.initialNumerator ? this.initialNumerator : 0
    window.eventHub.$on('increment', this.incrementCount)
    window.eventHub.$on('reset', this.reset)
  },
  beforeDestroy () {
    window.eventHub.$off('increment', this.incrementCount)
    window.eventHub.$off('delete-todo', this.reset)
  },
  methods: {
    incrementCount: function () {
      this.numerator++
    },
    reset: function () {
      this.numerator = 0
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
</style>
