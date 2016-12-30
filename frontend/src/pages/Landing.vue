<template>
<div>
<div class="landing-page">
	<header>
		<div class="container-fluid">
			<div class="logo-block">
				<img src="~assets/img/logo.svg" alt="Kanjisama logo" class="logo">
			</div>
			<div class="login-block">
				<a href="#" class="btn login-btn">login</a>
			</div>
		</div>
	</header>
	<main>
  <modal v-show="showLogin">
    <span slot="header">Login</span>
    <form slot="body">
      <input type="text" placeholder="email"> 
      <input type="text" placeholder="password"> 
      <span v-on:click="login">login</span>
    </form>
  </modal>
		<div class="welcome-block col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<div class="container-fluid">
				<div class="main">
					<h1 class="site-heading">Never get lost in translation again</h1>
					<p class="site-subheading">Get the reading skills you need to crush it in Japan</p>
				</div>
				<div class="get-trial-block">
					<a href="#" class="btn get-trial-btn">Get free trial</a>
				</div>
			</div>
		</div>
		<div class="why-us col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<h2 class="block-heading">Why Kanjisama?</h2>
			<div class="explanation col-lg-12 col-md-12">
				<div class="one-item col-lg-7 col-lg-offset-4 col-md-7 col-md-offset-4 col-sm-12 col-xs-12 col-xs-12-offset">
					<div class="icon-block upper">
						<img src="~assets/img/landing_page/icons/clock_icon.svg" alt="" class="icon">
					</div>
					<div class="text-block lower">
						<h3 class="heading">Save time.</h3>
						<p class="text">Hack your way through vocabulary and kanji, with a clever learning path that teaches you how to read Japanese, efficiently and quickly.</p>
					</div>
				</div>
				<div class="one-item second col-lg-7 col-lg-offset-1 col-md-7 col-md-offset-1 col-xs-12 col-xs-12-offset">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/book.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<h3 class="heading">Learn to read Japanese, not just <span class="italic">kanji.</span></h3>
						<p class="text">Knowing standalone kanji isn’t bad. But being able to read lots of actual words is much better. Kanjisama teaches you kanji in combination with actual words.</p>
					</div>
				</div>
				<div class="one-item col-lg-7 col-lg-offset-4 col-md-7 col-md-offset-4 col-xs-12 col-xs-12-offset">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/puzzle.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<h3 class="heading">Get exactly what you, and only you, need.</h3>
						<p class="text">Kanjisama allows you to adjust the pace you’re learning at. It also lets you easily skip words you already know, or add words you want to learn to your plan, on the fly.</p>
					</div>
				</div>
				<div class="one-item second col-lg-7 col-lg-offset-1 col-md-7 col-md-offset-1 col-xs-12 col-xs-12-offset">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/elephant_icon.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<h3 class="heading">Remember it for life.</h3>
						<p class="text">Kanjisama calculates the best time for you to repeat what you’ve learned, so that you can recall it whenever you need it.  Long term memory, dont forget after a month</p>
					</div>
				</div>
				<div class="one-item col-lg-7 col-lg-offset-4 col-md-7 col-md-offset-4 col-xs-12 col-xs-12-offset">
					<div class="icon-block upper">
						<img src="~assets/img/landing_page/icons/mama.svg" alt="" class="icon">
					</div>
					<div class="text-block last">
						<h3 class="heading">Give procrastination no chance!</h3>
						<p class="text">Kanjisama helps you stay on track. It’s like your mom, just without the reproachful look.</p>
					</div>
				</div>
			</div>
		</div>
		<div class="is-it-for-you col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<h3 class="block-heading">Is Kanjisama for you?</h3>
			<div class="pros col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-10 col-sm-offset-1 col-xs-12 col-xs-offset-0">
				<p class="pros-cons-heading">Kanjisama is for you, if you’re…</p>
				<ul class="list">
					<li>serious about learning to read Japanese. </li>
					<li>longing for somebody to guide you through <br>the lonely and rough path to becoming a real<br> kanji master. </li>
					<li>eager to find out what’s written on the 29 pages <br>of the Japanese menu that - for some <br>mysterious reason - didn't make it into the <br>one page English version. </li>
				</ul>
			</div>
			<div class="cons col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-10 col-sm-offset-1 col-xs-12 col-xs-offset-0">
				<p class="pros-cons-heading">Kanjisama is not for you, if…</p>
				<ul class="list">
					<li>your morning routine includes having the Nikkei <br>Shinbun with your coffee.</li>
					<li>you want to become a koala farmer. In that case,<br>I’d recommend you forget about Japanese, <br>andstart learning more about koalas. But, please <br>invite us to your farm, once you have one, <br>because we love koalas! </li>
				</ul>
			</div>
		</div>
		<div class="offer col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<h3 class="block-heading">What does Kanjisama offer?</h3>
			<div class="container">
				<div class="one-item col-lg-4 col-md-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/path_with_sun_icon.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Best practice<br>learning path</p>
					</div>
				</div>
				<div class="one-item col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/alarm_clock.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Smart timing and reminder<br>function for deepening <br>what you’ve learned <br>(Spaced Repetition System)</p>
					</div>
				</div>
				<div class="one-item col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/cards.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Comprehensive vocabulary <br>cards, including word <br>meaning, reading and <br>context of use</p>
					</div>
				</div>
				<div class="one-item col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/phone.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Mobile version, so that you <br>can learn whenever and <br>wherever you want</p>
					</div>
				</div>
				<div class="one-item col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/survacing.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Progress tracking and sur-<br>facing words you have <br>trouble remembering</p>
					</div>
				</div>
				<div class="one-item col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<div class="icon-block">
						<img src="~assets/img/landing_page/icons/koala_button.svg" alt="" class="icon">
					</div>
					<div class="text-block">
						<p class="one-offer">Koala button (figure that <br>one out by yourself...)</p>
					</div>
				</div>
			</div>
		</div>
		<div class="cta-block col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<h3 class="cta-heading">Wanna learn how to <br>read Japanese?</h3>
			<p class="cta-subheading">Try the beta version today, for free!</p>
			<div class="cta-btn-block">
				<a href="#" class="btn cta-btn">Get your free trial!</a>
			</div>
			<p class="btn-support-text">I am a huge button. Click me!</p>
		</div>
		<div class="about-block col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<h3 class="block-heading">About Kanjisama</h3>
			<div class="about-text col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-10 col-sm-offset-1 col-xs-12 col-xs-offset-0">
				<p class="text">It’s so frustrating when you ﬁgure out that you still cannot read and understand Japanese texts, although you’ve studied kanji for, like, fo’ eva. Right?!</p>
				<p class="text">I’ve learned kanji in school for years, but when I came to Japan, Japanese texts still looked like a weird mixture of Chinese and chicken footprints to me.</p>
				<p class="text">What does this say? “Visa application” or “toaster manual”?</p>
				<p class="text">Frustrating!</p>
				<p class="text">Kanjisama was developed to end this misery, once and for all.</p>
				<p class="text">Kanjisama helps you learn to actually read Japanese texts, and acquire the skills and knowledge you need to pursue your dreams in Japan. Without getting lost in translation!</p>
			</div>
			<div class="who-block col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-10 col-sm-offset-1 col-xs-12 col-xs-offset-0">
				<div class="author col-lg-12 col-md-12 col-sm-12">
					<div class="photo-block col-lg-4 col-md-5 col-sm-5 col-xs-5">
						<img src="~assets/img/landing_page/drew.png" alt="Drew Terry">
					</div>
					<div class="text-block col-lg-7 col-md-7 col-sm-7 col-xs-7">
						<p class="heading">Drew Terry</p>
						<p class="subheading">Founder of Kanjisama<br>(also known as ザーファウンダー)</p>
					</div>
				</div>
				<div class="koala col-lg-12 col-md-12 col-sm-12 col-xs-12">
					<div class="photo-block col-lg-5 col-md-5 col-sm-4 col-xs-4">
						<img src="~assets/img/landing_page/icons/koala_color.png" alt="Koalasama">
					</div>
					<div class="text-block col-lg-7 col-md-7 col-sm-8 col-xs-8">
						<p class="heading">Koalasama</p>
						<p class="subheading">Official Mascot of Kanjisama<br>(also known as ザーコアラー)</p>
					</div>
				</div>
			</div>
		</div>
	</main>
	<footer>
		<div class="footer-container col-lg-7 col-lg-offset-3 col-md-7 col-md-offset-3 col-sm-10 col-sm-offset-1 col-xs-10 col-xs-offset-1">
			<div class="nav-block">
				<ul>
					<li>
						<a href="#">Why Kanjisama</a>
					</li>
					<li>
						<a href="#">Is Kanjisama for you?</a>
					</li>
					<li>
						<a href="#">Features</a>
					</li>
					<li>
						<a href="#">Pricing</a>
					</li>
					<li>
						<a href="#">About</a>
					</li>
				</ul>
			</div>
			<div class="btns-block">
				<div class="sing-in-btn-block">
					<a href="#" class="btn sign-in-btn">Sign in</a>
				</div>
				<div class="sing-up-btn-block">
					<a href="#" class="btn sign-up-btn">Sign up</a>
				</div>
			</div>
		</div>
		<div class="socials">
			<div class="icons">
				<a href="#" class="social-icon fb">
					<img src="~assets/img/landing_page/fb.png" alt="">
				</a>
				<a href="#" class="social-icon twitter">
					<img src="~assets/img/landing_page/fb.png" alt="">
				</a>
			</div>
		</div>
		<div class="copyright-block">
			<a href="#" class="terms">Terms of Use and Privacy</a>
			<p class="copy">All Rights Reserved by Kanjisama</p>
		</div>
	</footer>

</div>

</div>
</template>

<script>
import ModalBase from '../components/ModalBase.vue'
export default {
  name: 'landingPage',
  data () {
    return {
      reviewDeck: [],
      errors: null,
      showLogin: true
    }
  },
  components: {
    'modal': ModalBase
  },
  methods: {
    login: function () {
      var url = '/login/auth/'
      this.$http.post(url)
      .then(response => {
        this.errors = null
        this.reviewDeck = response.data
/* eslint-disable */
      }, error => {
        this.errors = 'Could not fetch deck from server!'
      })
      console.log('gere')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "../assets/style/landing-page-css/style.scss";
</style>
