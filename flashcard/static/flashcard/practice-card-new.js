vocab.original_length = vocab.length;
vocab.sets_until_complete = 1;
var wordnumber = 0;
var current_word = vocab[wordnumber];
var input_ready = true;


//to do: add set complete popup, edit css of cards etc


function shuffleArray(an_array) {
    for (var i = an_array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = an_array[i];
        an_array[i] = an_array[j];
        an_array[j] = temp;
    }
    return an_array;
}



var startpage_2 = function(){
	//This is for outside case of only two words in stack
	try {
		// vocab[randarray[1]].word
		var vocab_word = vocab[1].word
	}catch(err){
		if(vocab.sets_until_complete == 1){
			var vocab_word = "...and again!";
		}else{
			var vocab_word = "Finish!";
		};
	};

	initial_cards = ''
 	initial_cards +=						'<div class = "container">	'
 	initial_cards +=						'	<div id = "flashcard-page-card-row" class = "row">'
	initial_cards +=	    				'  		<div class="col-xs-0 col-sm-3 col-md-3">'
 	initial_cards +=						'			<div class="flip-container">'
 	initial_cards +=						'				<div id = "array_place_' + wordnumber+1 + '" class="flipper mini-flipper">'
 	initial_cards +=						'					<div class="front text-center review-card mini-card">'
 	initial_cards +=												vocab_word
 	initial_cards +=						'					</div>'
 	initial_cards +=						'					<div class="back text-center review-card mini-card">'
 	initial_cards +=						'						test'
 	initial_cards +=						'					</div>'
	initial_cards +=						'					'
	initial_cards +=						'					'
 	initial_cards +=						'				</div>'
	initial_cards +=						'			</div>	'
 	initial_cards +=						'		</div>'
	initial_cards +=	    				'  		'
	initial_cards +=						'		'
	initial_cards +=	    				'  		<div class="col-xs-12 col-sm-12 col-md-6">'
 	initial_cards +=						'			<div id = "main-card" class="flip-container">'
 	initial_cards +=						'				<div id = "array_place_' + wordnumber + '" class="flipper main-flipper">'
 	initial_cards +=						'					<div class="front text-center review-card front-main">'
 	initial_cards +=											vocab[0].word
 	initial_cards +=						'					</div>'
 	initial_cards +=						'					<div class="back text-center review-card back-main align-vertical">'
	initial_cards +=						'						<p>' + vocab[0].hiragana + '</p>'
 	initial_cards +=						'					</div>'
 	initial_cards +=						'				</div>'
	initial_cards +=						'			</div>	'
 	initial_cards +=						'		</div>'
	                                 
	document.getElementById('card-container').innerHTML = initial_cards;
	
	write_info_box();
	
};



$('#answer-input').keydown(function(event){
	if(input_ready === true && event.keyCode === 13){
		var answer_input = document.getElementById('answer-input')
		var answer_input_value = document.getElementById('answer-input').value.toLowerCase();
		var english_def = current_word.definitions;
		
		var reset_input_bar = function(text_type,wrong_answer, delay_time){
			window.setTimeout(function(){
				var input_placeholder_text = text_type === "hiragana" ? "ひらがな" : "meaning"; 
				answer_input.placeholder = input_placeholder_text;
				if(wrong_answer){$("#main-card").toggleClass("flip")};
				answer_input.value = '';
				answer_input.style.color = "grey";
				input_ready = true;
			},delay_time);
		};
					
		//if user is submitting answer for hiragana
		if(current_word.hiragana_attempt === false){
			var hiragana_reading = current_word.hiragana;
			
			//if user submits correct answer
			if(hiragana_reading === answer_input_value){
				current_word.hiragana_correct = true;
				answer_input.style.color = "#19fc5d";
				
				reset_input_bar("meaning", false, 500);
				
			//if user submits incorrect answer	
			}else{
				answer_input.style.color = "#fc0527";
				$("#main-card").toggleClass("flip");
				input_ready = false;
				reset_input_bar("meaning",true,2000);
				
			};
			
			wanakana.unbind(inputIME);
			current_word.hiragana_attempt = true;
		
		//if user is submitting answer for definition	
		}else{
			
			$('.back > p').html(current_word.definitions.join("; "));
			
			//goes through each definition to see if any match user input
			for(var i = 0; i <= current_word.definitions.length - 1; i++){
				var clean_definitions = current_word.definitions[i].replace(/ *\([^)]*\) */g, "");
				var levenshteinenator_value = levenshteinenator(answer_input_value, clean_definitions.toLowerCase());
				var levenshteinenator_value_compare = levenshteinenator_value / clean_definitions.length;
				var correct_answer = levenshteinenator_value_compare <= .32;
				if(correct_answer == true){break}
			};
					
			if(correct_answer){
				current_word.english_def_correct = true;
				answer_input.style.color = "#19fc5d";
				var next_card_interval = 100;
				
				reset_input_bar("hiragana", false, 100);
				
			}else{
				console.log("not correct");
				answer_input.style.color = "#fc0527";
				wanakana.bind(inputIME);
				$("#main-card").toggleClass("flip");
				
				var next_card_interval = 2200;
					
				reset_input_bar("hiragana", true, 2000);
			};
			
			input_ready = false;
			wanakana.bind(inputIME);
			
			//reinserts word back into vocab list if any part is incorrect
			if(current_word.english_def_correct === false || current_word.hiragana_correct == false){
				
				current_word.hiragana_attempt = false;
				current_word.english_def_correct = false;
				current_word.hiragana_correct = false;
				if(vocab.length - wordnumber > 3){
					vocab.splice(wordnumber + 3, 0,current_word)
				}else{
					vocab.push(current_word);
				};
					
			}else{
				var current_remaining = $('#remaining-count').data('remaining');
				$('#remaining-count').data('remaining', current_remaining - 1);
				$('#remaining-count').html(current_remaining - 1);
				var completed_words = $('#completed-word-count').data('complete');
				$('#completed-word-count').data('complete', completed_words + 1);
				$('#completed-word-count').html(completed_words + 1);
			};
			window.setTimeout(function(){next_card_2()},next_card_interval);
			
		};
	};
});

$('#answer-form').submit(function(event){
	event.preventDefault();
});

//writes word information
var write_info_box = function(){

		definition_info = '';
		definition_info = current_word.definitions.join(", ");
		
		var kanji_symbols = '';
		for(var i = 0; i<=current_word.kanjis.length; i++){
			if(current_word.kanjis[i]){
				
				kanji_symbols += 			'<div class = "each-kanji information">';
				kanji_symbols +=				'<div class = "actual-kanji">'+ current_word.kanjis[i] + '</div>';
				kanji_symbols +=				'<div class = "kanji-meaning">'+ current_word.kanji_meanings[i] +'</div>';
				kanji_symbols +=			'</div>';
				
			};		
		};
		
		$('#word-reading').html(current_word.hiragana);
		$('#word-pos').html(current_word.part_of_speech.join('<br>'));
		$('.list-definitions').html(definition_info);
		$('.kanji-info').html(kanji_symbols);
		
};



var next_card_2 = function(){
	$(".mini-flipper").animate({
		"left":"275px",	
	},1);
	
	$(".main-flipper").animate({
		"left":"550px",	
	},1);
	
	$(".mini-card").animate({
		"height":"270px",
		"width":"520px",
		"margin-top":"0px",
		"line-height":"270px",
		"font-size":"4em",
	},600);
	
	$(".front-main").animate({
		"height":"135px",
		"width":"245px",
		"margin-top":"75px",
		"line-height":"115px",
		"font-size":"2em",
	},600);
	
	wordnumber += 1;
	current_word = vocab[wordnumber];
	input_ready = true;
	try{current_word.word
	}catch(err){
		window.setTimeout(reset_2,2000);
	};
	
	rewrite_cards_2();
	write_info_box();
};



var rewrite_cards_2 = function(){
	
	if(vocab.sets_until_complete === 0){
		var left_card_text = (wordnumber+1 < vocab.length) ? vocab[wordnumber + 1].word : "Finish!";
	}else{
		var left_card_text = (wordnumber+1 < vocab.length) ? vocab[wordnumber + 1].word : "...and again!";
	};	
	
	var rewritecards = '';
		rewritecards += '<div class = "container">	'
		rewritecards += ' 				<div id = "flashcard-page-card-row" class = "row">'
		rewritecards += '		      		<div class="col-xs-0 col-sm-3 col-md-3">'
		rewritecards += ' 						<div id = "first-card" class="flip-container">'
		rewritecards += ' 							<div class="flipper mini-flipper">'
		rewritecards += ' 								<div class="front text-center review-card mini-card">'
		rewritecards +=  									left_card_text
		rewritecards += ' 								</div>'
		rewritecards += ' 								<div class="back text-center review-card mini-card">'
		rewritecards += ' 									ing'
		rewritecards += ' 								</div>'
		rewritecards += '								'
		rewritecards += '								'
		rewritecards += ' 							</div>'
		rewritecards += '						</div>	'
		rewritecards += ' 					</div>'
		rewritecards += '		      		'
		rewritecards += '					'
		rewritecards += '		      		<div class="col-xs-12 col-sm-12 col-md-6">'
		rewritecards += ' 						<div id = "main-card" class="flip-container">'
		rewritecards += ' 							<div class="flipper main-flipper">'
		rewritecards += ' 								<div class="front text-center review-card front-main">'
		rewritecards +=  									 current_word.word
		rewritecards += ' 								</div>'
		rewritecards += ' 								<div class="back text-center review-card back-main align-vertical">'
		rewritecards += '									<p>' + current_word.hiragana + '</p>'
		rewritecards += ' 								</div>'
		rewritecards += ' 							</div>'
		rewritecards += '						</div>	'
		rewritecards += ' 					</div>'
		rewritecards += '					'
		rewritecards += '					'
		rewritecards += '					'
		rewritecards += '		      		<div class="col-md-3">'
		rewritecards += ' 						<div class="flip-container">'
		rewritecards += ' 							<div class="flipper mini-flipper">'
		rewritecards += ' 								<div class="front text-center review-card mini-card">'
		rewritecards +=  									vocab[wordnumber - 1].word
		rewritecards += ' 								</div>'
		rewritecards += ' 								<div class="back text-center review-card mini-card">'
		rewritecards += ' 									ing'
		rewritecards += ' 								</div>'
		rewritecards += ' 							</div>'
		rewritecards += '						</div>	'
		rewritecards += ' 					</div>'
		rewritecards += '				'
		rewritecards += '				</div>'
		rewritecards += '			</div>'
	
	window.setTimeout(function(){
		document.getElementById('card-container').innerHTML = rewritecards;
		$("#first-card").hide().fadeIn();
	},500);
};



var levenshteinenator = (function () {

	/**
	 * @param String a
	 * @param String b
	 * @return Array
	 */
	function levenshteinenator(a, b) {
		var cost;
		var m = a.length;
		var n = b.length;

		// make sure a.length >= b.length to use O(min(n,m)) space, whatever that is
		if (m < n) {
			var c = a; a = b; b = c;
			var o = m; m = n; n = o;
		}

		var r = []; r[0] = [];
		for (var c = 0; c < n + 1; ++c) {
			r[0][c] = c;
		}

		for (var i = 1; i < m + 1; ++i) {
			r[i] = []; r[i][0] = i;
			for ( var j = 1; j < n + 1; ++j ) {
				cost = a.charAt( i - 1 ) === b.charAt( j - 1 ) ? 0 : 1;
				r[i][j] = minimator( r[i-1][j] + 1, r[i][j-1] + 1, r[i-1][j-1] + cost );
			}
		}

		return r[r.length-1][r[r.length-1].length-1];
	}

	/**
	 * Return the smallest of the three numbers passed in
	 * @param Number x
	 * @param Number y
	 * @param Number z
	 * @return Number
	 */
	function minimator(x, y, z) {
		if (x < y && x < z) return x;
		if (y < x && y < z) return y;
		return z;
	}

	return levenshteinenator;

}());



var reset_2 = function(){
	
	if(vocab.sets_until_complete == 0){
		update_words();
		$('#completed-count').html(vocab.original_length)
		$('#myModal').modal('show');
		// console.log("woooork")
		
	}else{
		vocab.sets_until_complete = vocab.sets_until_complete - 1;
		wordnumber = 0;
		vocab.length = vocab.original_length;
		for(var i = 0; i < vocab.length; i++){
			vocab[i].hiragana_correct = false;
			vocab[i].english_def_correct = false;
			vocab[i].hiragana_attempt = false;
		};
		
		$("#word-info-panel").css('visibility','hidden');
		shuffleArray(vocab);
		$('#remaining-count').data('remaining', vocab.original_length);
		$('#remaining-count').html(vocab.original_length);
		$('#completed-word-count').data('complete',0);
		$('#completed-word-count').html(0);
		current_word = vocab[wordnumber];
		startpage_2();
	};
};



var update_words = function(signal){
	set_name = document.getElementById('set-name').value
	user_name = document.getElementById('user-name').value
	$.ajax({
		// need to pass variable to template that I can grab with javascript to replace this url
		// will not work on other profiles
		url:'/profile/' + user_name + '/' + set_name + '/complete-stack',
		type:'POST',
		data:{wordlist: JSON.stringify(vocab), csrfmiddlewaretoken: csrftoken, set_name: set_name},
		success: update_words_success, 
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
	
	var update_words_success = function(data){
		console.log(data);
	};
};


var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


startpage_2();



