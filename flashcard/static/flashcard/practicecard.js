
var troublewords = [];
var wordnumber = 0;
var remaining = vocab.length;
var randarray = [];

//creates array of random uniques
var randomarray = function(){
 randarray = [];

	while(randarray.length < vocab.length){
  	  	var randomnumber=Math.floor(Math.random() * vocab.length)
   	 	var found=false;
   	 	for(var i=0;i<randarray.length;i++){
        	if(randarray[i]==randomnumber){
        		found=true;break
        }
  	  }
  	  if(!found)randarray[randarray.length]=randomnumber;
	
	};
	console.log("this is the randarray " + randarray);
}

//generates new center card
var startpage = function(){
	
	randomarray();
	var randvocabword = vocab[randarray[wordnumber]];
	
	for(var i = 0; i<2; i++){
		document.getElementById('front' + i).innerHTML = vocab[randarray[i]].kanji;
		document.getElementById('back' + i).innerHTML = vocab[randarray[i]].english;
	}
}


//animates cards to the right
var nextset = function(){
	
	var addone = wordnumber + 1;
	var addtwo = wordnumber + 2;
	
	$(".cardhold").animate({
		"left":"33.3%"
	},500);

	$("#word" + wordnumber).animate({
		"height":"133px",
		"width":"45%",
		"margin-top":"40px",
	},500);
	
	$("#front" + wordnumber).animate({
		"line-height":"133px",
		"font-size":"20px"
	},500);

	$("#word" +addone).animate({
		"height":"200px",
		"width":"90%",
		"margin-top":"0px",
	},500);
	
	$("#front" +addone).animate({
		"line-height":"200px",
		"font-size":"60px"
	},500);
	
	if(wordnumber+1 == randarray.length){ 
		document.getElementById('answerinput').value = 'finished';
		document.getElementById('answerinput').style.color = "grey";
	}else{
		document.getElementById('answerinput').value = '';
		document.getElementById('answerinput').style.color = "grey";
	}
	
	console.log(wordnumber+2);
	console.log(randarray.length);
	var rewritecards = '';
	if(wordnumber+2 < randarray.length){
		rewritecards += "<div id = 'cardhold" + addtwo + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + addtwo + "' class = 'answerbox mini left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + addtwo + "' class = 'front mini2'>" + vocab[randarray[addtwo]].kanji + "</div>";
		rewritecards += "<div id = 'back" + addtwo + "' class = 'back mini2'></div>";
		rewritecards += "</div></div></div>";
		rewritecards += "<div id = 'cardhold" + addone + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + addone + "' class = 'answerbox left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + addone + "' class = 'front'>" + vocab[randarray[addone]].kanji + "</div>";
		rewritecards += "<div id = 'back" + addone + "' class = 'back'>" + vocab[randarray[addone]].english + "</div>";
		rewritecards += "</div></div></div>";
		rewritecards += "<div id = 'cardhold" + wordnumber + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + wordnumber + "' class = 'answerbox mini left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + wordnumber + "' class = 'front mini2'>" + vocab[randarray[wordnumber]].kanji + "</div>";
		rewritecards += "<div id = 'back" + wordnumber + "' class = 'back mini2'></div>";
		rewritecards += "</div></div></div>";
	}else{
		rewritecards += "<div id = 'cardhold" + addtwo + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + addtwo + "' class = 'answerbox mini left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + addtwo + "' class = 'front mini2'>finish line!</div>";
		rewritecards += "<div id = 'back" + addtwo + "' class = 'back mini2'></div>";
		rewritecards += "</div></div></div>";
		rewritecards += "<div id = 'cardhold" + addone + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + addone + "' class = 'answerbox left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + addone + "' class = 'front'>" + vocab[randarray[addone]].kanji + "</div>";
		rewritecards += "<div id = 'back" + addone + "' class = 'back'>" + vocab[randarray[addone]].english + "</div>";
		rewritecards += "</div></div></div>";
		rewritecards += "<div id = 'cardhold" + wordnumber + "' class = 'cardhold'>";	
		rewritecards += "<div id = 'word" + wordnumber + "' class = 'answerbox mini left'>";
		rewritecards += "<div class = 'flipper'>";
		rewritecards += "<div id = 'front" + wordnumber + "' class = 'front mini2'>" + vocab[randarray[wordnumber]].kanji + "</div>";
		rewritecards += "<div id = 'back" + wordnumber + "' class = 'back mini2'></div>";
		rewritecards += "</div></div></div>";
	};
	
	wordnumber += 1;
	window.setTimeout(function(){
		document.getElementById('center').innerHTML = rewritecards;
		$("#cardhold"+addtwo).hide().fadeIn();
	},500);
	
	
	
	
	
};


//on enter of text checks if correct answer, currently must be exact match but should change
$('#answerinput').keyup(function(event){
	if(event.keyCode == 13){
		
		var textinput = document.getElementById('answerinput');
		
		//checks entered word equals the english meaning
		if(textinput.value.indexOf(vocab[randarray[wordnumber]].english) == -1){
			$("#word" + wordnumber).toggleClass("answerbox2");
			textinput.style.color = "red";
			window.setTimeout(function(){
				$("#word" + wordnumber).toggleClass("answerbox2")
				document.getElementById('answerinput').value = '';
				document.getElementById('answerinput').style.color = "grey";
			},3000);
			
			if(wordnumber+1 != randarray.length){
				
				console.log("wrong");
				
				randarray.push(randarray[wordnumber]);
				
				//creates list of words missed in the first round
				if(troublewords.indexOf(randarray[wordnumber]) == -1){
					troublewords.push(randarray[wordnumber]);
					console.log("troubleword  " + troublewords);
					}
					
					textinput.style.color = "red";

				window.setTimeout(function(){nextset()},3200);
			}
			
		}else {
			console.log("this is correct");
			textinput.style.color = "rgba(66,235,89,1)";
			window.setTimeout(function(){nextset()},500);
			remaining -= 1
			document.getElementById('highscore').innerHTML = remaining;			
			
		}	
		console.log(randarray);	
	};
});





var reset = function(){
	remaining = vocab.length;
	document.getElementById('highscore').innerHTML = remaining;
	
	startpage();
}


//on page load
startpage();
document.getElementById('highscore').innerHTML = remaining;
document.getElementById('currentscore').onclick = function(){console.log(troublewords);};
document.getElementById('highscore').onclick = function(){
	reset();
};