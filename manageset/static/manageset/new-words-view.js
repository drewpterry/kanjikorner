$('#new-words').addClass('manageset-nav-selected');



var filter = "grade";

//addcheck holds the ids so when you search words it knows which ones have been highlighted or not
var addcheck = [];
//will hold ids of added words
var knowncheck = [];
var keyword = '';





$('#loadingDiv').hide()




var indicate_as_known = function(word_id){
	
	user_name = document.getElementById('user-name').value;
	$.ajax({
		// need to pass variable to template that I can grab with javascript to replace this url
		// will not work on other profiles
		url:'/profile/' + user_name + '/new-set/add-known-word',
		type:'POST',
		data:{word_id: word_id, csrfmiddlewaretoken: csrftoken},
		success: console.log('worked1'), 
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
};

var undo_indicate_as_known = function(word_id){
	
	user_name = document.getElementById('user-name').value;
	$.ajax({
		// need to pass variable to template that I can grab with javascript to replace this url
		// will not work on other profiles
		url:'/profile/' + user_name + '/new-set/remove-known-word',
		type:'POST',
		data:{word_id: word_id, csrfmiddlewaretoken: csrftoken},
		success: console.log('worked2'), 
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

	if(element.innerText == "add"){
			
		var hiddeninput = "<input type = 'hidden' id = 'chosenwords" + idnumber + "' name = 'chosenwords' value = '" + idnumber +"' ></input>";
		
		$("#create-set-form").prepend(hiddeninput); 
		$("#wordlist-new").append(minicard);
		//array that holds ids of selected words
		addcheck.push(idnumber);
		// permanently add outline to added card or removes it if remove is clicked
		element.parentNode.className += " outline";
		element.innerHTML = "remove";
		element.previousSibling.previousSibling.disabled = true;
		selected_word = $('#answercontainer'+idnumber).find('#kanji').text()
		console.log(selected_word)
		for(var i = 0; i <= the_selected_kanji.length; i++){
			
			
			if(selected_word.indexOf(the_selected_kanji[i]) != -1){
				console.log('got here');
				var kanji_used_count = $('#filter-' + the_selected_kanji[i]).data("count");
				var new_count = kanji_used_count + 1
				$('#filter-' + the_selected_kanji[i]).data("count", new_count);
				$('#filter-' + the_selected_kanji[i]).find(".kanji-count").text(new_count);
			};
				
		};
		
	}else{
		//i think i still need this
		removeWord(idnumber, kanji, meaning, this)
		for(var i = 0; i <= the_selected_kanji.length; i++){
			
			
			if(selected_word.indexOf(the_selected_kanji[i]) != -1){
				console.log('got here');
				var kanji_used_count = $('#filter-' + the_selected_kanji[i]).data("count");
				var new_count = kanji_used_count - 1
				$('#filter-' + the_selected_kanji[i]).data("count", new_count);
				$('#filter-' + the_selected_kanji[i]).find(".kanji-count").text(new_count);
			};
				
		};
		

	};
};



var know_it = function(idnumber, kanji, meaning, element){
	the_card = $('#answercontainer'+idnumber);
	the_card.find('.front').css('opacity',.4);
	element.disabled = true;
	element.nextSibling.nextSibling.disabled = true;
	the_card.find('.undo').css('visibility','visible');
	indicate_as_known(idnumber);
	
	
	
};

var undo = function(idnumber, kanji, meaning, element){
	the_card = $('#answercontainer'+idnumber);
	the_card.find('.front').css('opacity',1);
	the_card.find('#knowit').removeAttr('disabled');
	the_card.find('#addit').removeAttr('disabled');
	the_card.find('.undo').css('visibility','hidden');
	the_card.css('cursor','auto');
	undo_indicate_as_known(idnumber)
};


var removeWord = function(idnumber, kanji, meaning, element){
	
	// element.innerHTML = "add";
	// element.parentNode.className = "front";
	
	var wordCard = $('#answercontainer'+idnumber);
	document.getElementById('answercontainerdif'+idnumber).remove();
	// document.getElementById('chosenwords'+idnumber).remove();
	//removes hidden field
	if (wordCard.find('#knowit').is(':disabled')){
		document.getElementById('chosenwords'+idnumber).remove();
		wordCard.find('#addit').html('add');
		wordCard.find('#knowit').removeAttr('disabled');
		// wordCard.children[3].disabled = false;
		//removing id from array
		var position = addcheck.indexOf(idnumber);
		addcheck.splice(position,1);
		
		
	}else{
		document.getElementById('knownwords'+idnumber).remove();
		wordCard.find('#knowit').html('know it!');
		wordCard.find('#addit').removeAttr('disabled');
		
		
		var position = knowncheck.indexOf(idnumber);
		knowncheck.splice(position,1);
	};
	

	wordCard.children().children('.front').attr('class','front');
	
// 	wordCard.children[3].innerHTML = "know it!";
// 	wordCard.lastChild.disabled = false;
//
	
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



		