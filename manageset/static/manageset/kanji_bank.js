$('#kanji-bank').addClass('manageset-nav-selected');


var filter = "grade";

//addcheck holds the ids so when you search words it knows which ones have been highlighted or not
var addcheck = [];
//will hold ids of added words
var keyword = '';



var search = function(signal){
	
	$.ajax({
		url:'/profile/new-set/get-known-kanji',
		type:'GET',
		data:{theorder: filter , csrfmiddlewaretoken: '{{ csrf_token }}', searchword: keyword},
		success: displaySearch, 
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
};


$('#loadingDiv').hide()


var addword = function(idnumber, kanji, meaning, element){
	
	
	var minicard =''; 
	minicard = minicard + "<div id = 'answercontainerdif" + idnumber + "' class = 'answerbox mini'>";
	minicard = minicard + "<div class = 'flipper'><div class = 'front mini' onclick = 'removeWord(" + idnumber + ",\"" + kanji + "\",\"" + meaning + "\", this)'>"; 
	minicard = minicard + "<div id = 'red-ex'>X</div>"
	minicard = minicard + "<div id = 'kanji'>" + kanji + "</div>";
	minicard = minicard + "<div id = 'meaning'>" + meaning + "</div>";
	minicard = minicard + "</div></div>"
	minicard = minicard + "<div class = 'back mini'>" + kanji + "</div></div></div>";

	if(element.innerText == "Remove"){

		var hiddeninput = "<input type = 'hidden' id = 'chosenwords" + idnumber + "' name = 'chosenwords' value = '" + idnumber +"' ></input>";

		$("#remove-kanji-form").prepend(hiddeninput);
		$("#wordlist-know").append(minicard);
		//array that holds ids of selected words
		addcheck.push(idnumber);
		// permanently add outline to added card or removes it if remove is clicked
		element.parentNode.className += " outline";
		element.innerHTML = "undo";
		element.previousSibling.disabled = true;


		
	}else{
		
		removeWord(idnumber, kanji, meaning, this)
		
	};
};




var removeWord = function(idnumber, kanji, meaning, element){
	

	
	var wordCard = document.getElementById('answercontainer'+idnumber).firstChild.firstChild;
	document.getElementById('answercontainerdif'+idnumber).remove();
	
		document.getElementById('chosenwords'+idnumber).remove();
		wordCard.lastChild.innerHTML = "add";
		wordCard.children[3].disabled = false;
		//removing id from array
		var position = addcheck.indexOf(idnumber);
		addcheck.splice(position,1);


	wordCard.className = "front";
	wordCard.children[3].innerHTML = "Remove";
	wordCard.lastChild.disabled = false;
	
	
}




//add remov red x on hover
$("#wordlist-know").on("mouseover",".front", function(){
	$(this).children("#red-ex").show();
});

$("#wordlist-know").on("mouseout",".front", function(){
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

	data = JSON.parse(data);


	var dataLength = data.length;
	var foundflag = false;
	var content = ''
	var addCheckLength = addcheck.length;
		

	
	for(var i= 0; i<dataLength; i++){
		var pk = data[i].pk;
		var kanjiName = data[i].fields.kanji_name;
		var kanjiMeaning = data[i].fields.kanji_meaning;

			content = content + "<div id = 'answercontainer" + pk + "' class = 'answerbox' data-id = '"+ pk +"' >";
			content = content + "<div class = 'flipper'><div class = front><button class = 'special-kanji-switch'>✓</button>";
			content = content + "<div id = 'kanji'>" + kanjiName + "</div>";
			content = content + "<div id = 'meaning'>" + kanjiMeaning + "</div>";
			content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
			//hmmm some people on stackoverflow say inline javascript is bad practice...
			//also probably the fact that I repeat it 2 times is bad...
			content = content + "<button class = 'add-remove' onclick = 'addword(" + pk + ",\"" + kanjiName + "\",\"" + kanjiMeaning + "\", this)'>Remove</button>";
			content = content + "</div></div>"
			content = content + "<div class = 'back'>" + kanjiName + "</div></div></div>";

		};
	document.getElementById('container').innerHTML = content;
	
	for (var i = 0; i <= selected_kanji_list.length; i++){
		console.log(i)
		$('#answercontainer'+selected_kanji_list[i]).find('div .special-kanji-switch').addClass("selected-kanji");
	};	



		for(var i = 0; i<addCheckLength; i++){
			if(document.getElementById('answercontainer'+addcheck[i]) != null){

				//this should probably somehow be combined with the bit in addword function, also made more clear what its targeting
				//add class to div where class = front
				document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.className += " outline";
				//change add button to a remove button
				document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.lastChild.innerHTML = "remove";
			}
		}
		
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
search('');

$("#container").on("click", ".special-kanji-switch", function(){
	// console.log("clicking this button worked");
	theclass = this.className;
	if (theclass == "special-kanji-switch"){
		this.classList.add("selected-kanji");
	}else{
		this.classList.remove("selected-kanji");
	};
	
	kanji_id = this.parentNode.parentNode.parentNode.dataset.id
	console.log(kanji_id)
	$.ajax({
		url:'/profile/upate-knownkanji-special',
	//need to make this a post request
		type:'GET',
		data:{theid: kanji_id , csrfmiddlewaretoken: '{{ csrf_token }}'},
		success: function(data){
			
	console.log(data);
},
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
});		

$('#answercontainer26').find('div .special-kanji-switch').addClass("selected-kanji")
// $('#answercontainer26').childNode.childNode


