$('#new-kanji').addClass('manageset-nav-selected');

var filter = "grade";

//addcheck holds the ids so when you search words it knows which ones have been highlighted or not
var addcheck = [];
//will hold ids of added words
var keyword = '';



var search = function(signal){
	
	$.ajax({
		url:'/profile/new-set/word-search',
		type:'GET',
		data:{theorder: filter , csrfmiddlewaretoken: '{{ csrf_token }}', searchword: keyword},
		success: displaySearch, 
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
};




var addword = function(idnumber, kanji, meaning, element){
	
	
	var minicard =''; 
	minicard = minicard + "<div id = 'answercontainerdif" + idnumber + "' class = 'answerbox mini'>";
	minicard = minicard + "<div class = 'flipper'><div class = 'front mini' onclick = 'removeWord(" + idnumber + ",\"" + kanji + "\",\"" + meaning + "\", this)'>"; 
	minicard = minicard + "<div id = 'red-ex'>X</div>"
	minicard = minicard + "<div id = 'kanji'>" + kanji + "</div>";
	minicard = minicard + "<div id = 'meaning'>" + meaning + "</div>";
	minicard = minicard + "</div></div>"
	minicard = minicard + "<div class = 'back mini'>" + kanji + "</div></div></div>";

	
	if (element.innerText == "know it!"){
		var hiddeninput = "<input type = 'hidden' id = 'knownwords" + idnumber + "' name = 'known-kanji' value = '" + idnumber +"' ></input>";
		
		$("#wordlist-know").append(minicard);
		$("#known-kanji-form").prepend(hiddeninput);
		knowncheck.push(idnumber);
		element.parentNode.className += " outline-2";
		element.innerHTML = "remove";
		// element.nextSibling.disabled = true;
		
	}else{
		
		removeWord(idnumber, kanji, meaning, element)
		
	};
};




var removeWord = function(idnumber, kanji, meaning, element){
	
	
	document.getElementById('answercontainerdif'+idnumber).remove();
	var wordCard = element;
	console.log(wordCard);

	document.getElementById('knownwords'+idnumber).remove();
	var position = knowncheck.indexOf(idnumber);
	knowncheck.splice(position,1);
	
	wordCard.parentNode.className = "front";
	wordCard.innerHTML = "know it!";
	
	
	
}




//add remov red x on hover
$("#wordlist-new").on("mouseover",".front", function(){
	$(this).children("#red-ex").show();
});

$("#wordlist-new").on("mouseout",".front", function(){
	$(this).children("#red-ex").hide();
});





//filter options
$("#search-area").on("click",".filter", function(){
	
	keyword = document.getElementById('searchbox').value;
	
	if(this.id == "allwords"){
		document.getElementById('searchbox').value = '';
		search('');
		
	}else{
	
		if(this.id == "strokes"){
			filter = "strokes";
			
		}else if(this.id == "gradefilter"){
			filter = "grade";
			
		}else{
			console.log(this.id + "not implemented")
		};
		
		search('yes');
	};
});



var displaySearch = function(data,signal){
			data = JSON.stringify(data);
			data = JSON.parse(data);


			var dataLength = data.length;
			var foundflag = false;
			var content = ''
			var addCheckLength = addcheck.length;



				for(var i=0; i<dataLength; i++){
					var pk = data[i].pk;
					var kanjiName = data[i].fields.kanji_name;
					var kanjiMeaning = data[i].fields.kanji_meaning;

					// if(knowncheck.indexOf(pk.toString()) == -1){


						content = content + "<div id = 'answercontainer" + pk + "' class = 'answerbox' >";
						content = content + "<div class = 'flipper'><div class = front>";
						content = content + "<div id = 'kanji'>" + kanjiName + "</div>";
						content = content + "<div id = 'meaning'>" + kanjiMeaning + "</div>";
						content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
						content = content + "<button class = 'add-remove' id = 'knowit' onclick = 'addword(" + pk + ",\"" + kanjiName + "\",\"" + kanjiMeaning + "\", this)' >know it!</button>";
						//hmmm some people on stackoverflow say inline javascript is bad practice...
						//also probably the fact that I repeat it 2 times is bad...
						content = content + "<button class = 'add-remove' onclick = 'addword(" + pk + ",\"" + kanjiName + "\",\"" + kanjiMeaning + "\", this)'>add</button>";
						content = content + "</div></div>"
						content = content + "<div class = 'back'>" + kanjiName + "</div></div></div>";
					// }
				};
				document.getElementById('container').innerHTML = content;




					for(var i = 0; i<addCheckLength; i++){
						if(document.getElementById('answercontainer'+addcheck[i]) != null){

							//this should probably somehow be combined with the bit in addword function, also made more clear what its targeting
							//add class to div where class = front
							document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.className += " outline";
							//change add button to a remove button
							document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.lastChild.innerHTML = "remove";
						}
					}

// UNDO THE DISPLAY SEARCH FROM HERE ON UP!???????????????//////////////////////////////////////////////


					for(var i = 0; i<knowncheck.length; i++){
						if(document.getElementById('answercontainer'+knowncheck[i]) != null){

							//this should probably somehow be combined with the bit in addword function, also made more clear what its targeting
							//add class to div where class = front
							document.getElementById('answercontainer'+knowncheck[i]).firstChild.firstChild.className += " outline-2";
							//change add button to a remove button
							document.getElementById('answercontainer'+knowncheck[i]).firstChild.firstChild.lastChild.innerHTML = "remove";
						}
					}



		};
		
		
//so that opening page has all the cards
// search('');
		
