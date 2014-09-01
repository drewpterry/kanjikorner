

var filter = "grade";
var addcheck = [];
var keyword = '';

var search = function(signal){
	
	$.ajax({
		url:'http://localhost:8000/profile/new-set/word-search',
		type:'GET',
		data:{theorder: filter , csrfmiddlewaretoken: '{{ csrf_token }}', searchword: keyword},
		success: displaySearch, 
		failure: function(data){
			alert("Sorry got an error")
		}
	});
};


var addword = function(idnumber, kanji, meaning, element){
	
	if(element.innerText == "add"){
		var hiddeninput = "<input type = 'hidden' id = 'chosenwords" + idnumber + "' class = 'text-area left-margin' name = 'chosenwords' value = '" + idnumber +"' ></input>";
		$("#create-set-form").prepend(hiddeninput); 
	
		var minicard =''; 
		minicard = minicard + "<div id = 'answercontainerdif" + idnumber + "' class = 'answerbox mini'>";
		minicard = minicard + "<div class = 'flipper'><div class = 'front mini' onclick = 'addword(" + idnumber + ",\"" + kanji + "\",\"" + meaning + "\", this)'>"; 
		minicard = minicard + "<div id = 'red-ex'>X</div>"
		minicard = minicard + "<div id = 'kanji'>" + kanji + "</div>";
		minicard = minicard + "<div id = 'meaning'>" + meaning + "</div>";
		minicard = minicard + "</div></div>"
		minicard = minicard + "<div class = 'back mini'>" + kanji + "</div></div></div>";
	
		$("#wordlist").prepend(minicard);
		
		//array that holds ids of selected words
		addcheck.push(idnumber);
		
		// permanently add outline to added card or removes it if remove is clicked
		element.parentNode.className += " outline";
		element.innerHTML = "remove";
	}else{
		element.innerHTML = "add";
		element.parentNode.className = "front";
		document.getElementById('answercontainerdif'+idnumber).remove();
		//removes hidden field
		document.getElementById('chosenwords'+idnumber).remove();
		//removing id from array
		var position = addcheck.indexOf(idnumber);
		addcheck.splice(position,1);
		//this causes error
		document.getElementById('answercontainer'+idnumber).firstChild.firstChild.className = "front";
		document.getElementById('answercontainer'+idnumber).firstChild.firstChild.lastChild.innerHTML = "add";
	};
};


//Need to add hover over hover out of red x
$("#wordlist").on("mouseover",".front", function(){
	$(this).children("#red-ex").show();
});

$("#wordlist").on("mouseout",".front", function(){
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


// document.getElementById('searchbutton').onclick = function(){
//
// 	search("yes");
// };

var displaySearch = function(data,signal){

			data = JSON.parse(data);


			// if (signal == ''){
// 				keyword = '';
// 			}else{
// 			keyword = document.getElementById('searchbox').value;
// 			};
			var dataLength = data.length;
			var foundflag = false;
			var content = ''
			var addCheckLength = addcheck.length;
		

			// if(keyword == ''){
				for(var i= 0; i<dataLength; i++){
					var pk = data[i].pk;
					var kanjiName = data[i].fields.kanji_name;
					var kanjiMeaning = data[i].fields.kanji_meaning;

						content = content + "<div id = 'answercontainer" + pk + "' class = 'answerbox' >";
						content = content + "<div class = 'flipper'><div class = front>";
						content = content + "<div id = 'kanji'>" + kanjiName + "</div>";
						content = content + "<div id = 'meaning'>" + kanjiMeaning + "</div>";
						content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
						content = content + "<button class = 'add-remove'>know it!</button>";
						//hmmm some people on stackoverflow say inline javascript is bad practice...
						//also probably the fact that I repeat it 3 times is bad...
						content = content + "<button class = 'add-remove' onclick = 'addword(" + pk + ",\"" + kanjiName + "\",\"" + kanjiMeaning + "\", this)'>add</button>";
						content = content + "</div></div>"
						content = content + "<div class = 'back'>" + kanjiName + "</div></div></div>";

					};
				document.getElementById('container').innerHTML = content;


			// }else{
// 				var kanjiLowercase = keyword.toLowerCase();
// 				for(var i= 0; i<dataLength; i++){
//
// 					if(data[i].fields.kanji_meaning.toLowerCase().indexOf(kanjiLowercase)!= -1){
// 					//||data[i].fields.kanji_name.indexOf(keyword)!=-1){
// 						var pk = data[i].pk;
// 						var kanjiName = data[i].fields.kanji_name;
// 						var kanjiMeaning = data[i].fields.kanji_meaning;
//
// 						content = content + "<div id = 'answercontainer" + pk + "' class = 'answerbox' onclick = 'clicked(this)'>";
// 						content = content + "<div class = 'flipper'><div class = front>";
// 						content = content + "<div id = 'kanji'>" + kanjiName + "</div>";
// 						content = content + "<div id = 'meaning'>" + kanjiMeaning + "</div>";
// 						content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
// 						content = content + "<button class = 'add-remove'>know it!</button>";
// 						content = content + "<button class = 'add-remove'";
// 						content = content + "onclick = 'addword(" + pk + ",\"" + kanjiName + "\",\"" + kanjiMeaning + "\", this)'>add</button>";
// 						content = content + "</div></div>"
// 						content = content + "<div class = 'back'>" + kanjiName + "</div></div></div>";
// 						foundflag = true;
//
// 					};
//
// 					if(foundflag == true){
//
// 						document.getElementById('container').innerHTML = content;
//
// 					}else{
// 						document.getElementById('container').innerHTML = "There are no matching results for your query: " + keyword ;
// 					};
//
// 				}

			// }
				// document.getElementById('container').innerHTML = content;

					for(var i = 0; i<addCheckLength; i++){
						if(document.getElementById('answercontainer'+addcheck[i]) != null){

							//this should probably somehow be combined with the bit in addword function, also made more clear what its targeting
							//add class to div where class = front
							document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.className += " outline";
							//change add button to a remove button
							document.getElementById('answercontainer'+addcheck[i]).firstChild.firstChild.lastChild.innerHTML = "remove";
						}
					}
		};
//so that opening page has all the cards
search('');
		
