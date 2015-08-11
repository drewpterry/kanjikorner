// allows you to remove entire nodes
Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = 0, len = this.length; i < len; i++) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}


var disable_or_enable_submit_button = function(){
	if(stack_id_array.values.length === 0){
		document.getElementById('stack-submit').disabled = true;
	}else{
		document.getElementById('stack-submit').disabled = false;
	};
};

var stack_id_array = (function(){
	var ids = [];
	
	function add_or_remove_id(id){
		var index = ids.indexOf(id);
		if(index == -1){
			ids.push(id);
		}else{
			ids.splice(index,1);
		};
	};
		
	function disable_or_enable_submit_button(){
		if(stack_id_array.values.length === 0){
			document.getElementById('stack-submit').disabled = true;
		}else{
			document.getElementById('stack-submit').disabled = false;
		};
	};	
	
	return {
		values: ids,
		update_array: function(id){
			add_or_remove_id(id);
			disable_or_enable_submit_button();
		}	
	}	
})();

var add_word_to_stack = function(element, word_id, word_meaning, full_word){
	var already_clicked = element.data('clicked', true);
	element.addClass('add-word-button-clicked');
	element.html('Add ✓');
	var hiddeninput = "<input type = 'hidden' id = 'chosenwords" + word_id + "' name = 'chosenwords' value = '" + word_id +"' ></input>";
	$("#create-set-form").prepend(hiddeninput);
	
	var stack_preview_card = '';
	stack_preview_card 	+=	'<div id = "' + word_id + '" class = "col-xs-12 col-sm-12 col-md-12 preview-card">';
	stack_preview_card 	+=		'<span class = "pull-left">' + full_word + '</span><span class = "pull-right mini-word-meaning">' + word_meaning + '</span>';
	stack_preview_card  +=	'<hr></div>';
	$('#stack-preview').append(stack_preview_card);
	
	stack_id_array.update_array(word_id);
};

var click_button_if_in_stack = function(){
	
	for(var i = 0; i < stack_id_array.values.length; i++){
		var element = $('.add-word-button[data-id=' + stack_id_array.values[i] + ']');
		element.addClass('add-word-button-clicked');
		element.html('Add ✓');
		element.data('clicked', true);
	};
};

var remove_word_from_stack = function(element, word_id){
	element.removeClass('add-word-button-clicked');
	element.html('Add <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>');
	$("#" + word_id).remove();
	document.getElementById('chosenwords' + word_id).remove();
	var already_clicked = element.data('clicked', false);
	stack_id_array.update_array(word_id);	
};


// clicking the x button in top right hand corner of card
$('.remove-word-button').on('click', function(){
	var element = $(this);
	var word_id = element.data('id');
	var already_clicked = element.data('clicked');
	remove_word_or_undo(word_id, already_clicked, element);
});

var remove_word_or_undo = function(word_id, already_clicked, element){
	
	var user_name = document.getElementById('user-name').value;
	
	if(already_clicked === false){
		var url_route = 'add';
		element.data('clicked',true);
		element.addClass('red-color');
		
	}else{
		var url_route = 'remove';
		element.data('clicked',false);
		element.removeClass('red-color');
	};
	
	$.ajax({
		url:'/profile/' + user_name + '/new-set/' + url_route + '-known-word',
		type:'POST',
		data:{word_id: word_id, csrfmiddlewaretoken: csrftoken},
		success: console.log('worked1'),
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
};

var attach_kanji_info_click = function(){
	$('.glyphicon-info-sign').on('click', function(){
		var element = $(this).parent().find('.add-word-button');
		var kanji = element.data('kanji');
		var meaning = element.data('meaning');
		var grade = element.data('grade');
		var readings = element.data('readings');
		var strokes = element.data('strokes');
		$('#kanji-symbol').html(kanji);
		$('#readings').html(readings);
		$('#meaning').html(meaning);
		$('#grade').html(grade);
		$('#strokes').html(strokes)
		$('#myModal').modal('show');
	})
};

var attach_entry_button_click = function(){
	$('.add-word-button').on('click',function(){
		var element = $(this);
		var word_id = element.data('id');
		var word_meaning = element.data('meaning');
		var full_word = element.data('entry');
		var already_clicked = element.data('clicked');
		
		if(already_clicked === false){
			add_word_to_stack(element, word_id, word_meaning, full_word);
		}else{
			remove_word_from_stack(element, word_id);
		}
	});
};

var attach_word_info_click = function(){
	$('.word-info-click').on('click', function(){
		var element = $(this).parent().find('.add-word-button');
		var word = element.data('word');
		var reading = element.data('readings');
		var definitions = element.data('definitions');
		var pos = element.data('pos');
		var kanjis = element.data('kanjis');
		var kanji_meanings = element.data('kanji-meaning').split(',');
		var kanji_symbols = '';
		
		for(var i = 0; i<=kanjis.length - 1; i++){
				kanji_symbols += 			'<div class = "each-kanji information">';
				kanji_symbols +=				'<div class = "actual-kanji">'+ kanjis[i] + '</div>';
				kanji_symbols +=				'<div class = "kanji-meaning">'+ kanji_meanings[i] +'</div>';
				kanji_symbols +=			'</div>';
		};
		
		$('#word-info-header').html(word);
		$('#word-reading').html(reading);
		$('#word-pos').html(pos);
		$('.list-definitions').html(definitions);
		$('.kanji-info').html(kanji_symbols);
		$('#infoModal').modal('show');
	});
};


$('#filter-button').on('click', function(){
	$('#myModalFilter').modal('show');
});


// executed on page load
var get_known_kanji = (function(signal){
	
	user_name = document.getElementById('user-name').value;
	$('#filter-area').html("<img src = '/static/manageset/ajax-loader.gif'>")
	$('#filter-area').load('/profile/' + user_name + '/new-set/known-kanji-filter', function(){
		
		$('.filter-checkbox').on('click',function(){
			var element = $(this);
			element.toggleClass('filter-checked');
			var kanji_id = element.data('id');
			update_filter_kanji(kanji_id);
			filter_changed.change_filter(kanji_id);
		});
	});	
})();

var filter_changed = (function(){
	var filter_array = [];
	function add_to_filter_array(id){
		var index = filter_array.indexOf(id);
		if(index >= 0){
			filter_array.splice(index,1)
		}else{
			filter_array.push(id);
		}
	};
	
	return {
		change_filter: function(id){
			add_to_filter_array(id)
		},
		state: function(){
			var array_not_empty = filter_array.length != 0 ? true : false;
			return array_not_empty
		},
		
		reset: function(){
			filter_array = [];
		}
	}
})();

var update_filter_kanji = function(kanji_id){
	
	$.ajax({
		url:'/profile/upate-knownkanji-special',
	//should make this a post request
		type:'GET',
		data:{theid: kanji_id , csrfmiddlewaretoken: '{{ csrf_token }}'},
		success: function(data){

		},
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});
	
	//on clicking out of modal 
	$('#myModalFilter').on('hide.bs.modal', function (e) {
		if(filter_changed.state()){
		
			$('#your-words-container').html("<img class = 'center-block' src = '/static/manageset/ajax-loader.gif'>");
			$('#your-words-container').load('/profile/' + user_name + '/new-set/new-words', function(){
				attach_word_info_click();
				attach_entry_button_click();
			});
			$('#filter-well').load('/profile/' + user_name + '/new-set/selected-words');
			filter_changed.reset();
		}else{
			console.log('do nothing')
		}	
	})
};

$('#your-words').on('click',function(){
	
	$('#your-words-container').html("<img class = 'center-block' src = '/static/manageset/ajax-loader.gif'>");
	$('#your-words-container').load('/profile/' + user_name + '/new-set/new-words', function(){
		attach_word_info_click();
		attach_entry_button_click();
		click_button_if_in_stack();
	});
	$(this).addClass('button-clicked');
	$('#all-words').removeClass('button-clicked');
	$('#your-words-filter').show();
	$('#your-words-search').hide();
	$('#section-explanation').html("These words only consist of the kanji you've added organized by their relative frequency.");
});

$('#all-words').on('click',function(){
	// get_all_words();
	$('#your-words-container').html("<div class = 'row text-center'><h2>Search for words and they'll appear here!</h2></div>")
	$(this).addClass('button-clicked');
	$('#your-words').removeClass('button-clicked');
	$('#section-explanation').html('These are all the words organized by relative frequency.');
	$('#your-words-filter').hide();
	$('#your-words-search').show();
});

$('#search-button').on('click', function(){
	search_term = document.getElementById('search-input').value;
	console.log(search_term)
	get_all_words(search_term);
});

var get_all_words = function(search_term){
	user_name = document.getElementById('user-name').value;
	$('#your-words-container').html("<img class = 'center-block' src = '/static/manageset/ajax-loader.gif'>");
	$.post('/profile/' + user_name + '/new-set/all-words',{ search_word: search_term })
		.done(function( data ) {
			console.log(data)
			$('#your-words-container').html(data)
			attach_word_info_click();
			attach_entry_button_click();
			click_button_if_in_stack();		
	  });
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


//on page load
attach_kanji_info_click();
attach_word_info_click();
attach_entry_button_click();