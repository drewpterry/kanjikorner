<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <!--<hello></hello>-->
    <!--<router-link to="/review/lvl-2/3">Riskssssd</router-link>-->
    <!--<router-link to="/review/srs">Review ssrs</router-link>-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
@import '../node_modules/bootstrap/dist/css/bootstrap.css';
@import "assets/style/app.scss";
</style>
