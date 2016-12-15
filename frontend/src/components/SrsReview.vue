<template>
<div>
  <div class="top-progress">
    <div class="top-progress__inner" style="width: 76%"></div>
  </div>

  <div class="green-cover">
    <div class="row green-cover__head">
      <div class="col-md-2 col-sm-1">
        <router-link to="/">
          <div class="logo">
            <img src="../assets/img/logo-white.svg" alt="">
          </div>
        </router-link>
      </div>
      <div class="col-md-offset-9 col-md-1">
        <p class="green-cover__progress">2 / 20</p>
      </div>
    </div>
    <div class="container green-cover__body">
      <div class="row ">
        <div class="col-md-offset-2 col-md-8">
          <div class="panel panel-task">
            單詞
          </div>
          <div class="panel panel-answer">
            <input type="text" class="c-textarea" title="your answer" cols="30" rows="5">
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
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'srsreview',
  data () {
    return {
      msg: 'SRS REview'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
