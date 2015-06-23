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

$('.add-word-button').on('click',function(){
	var element = $(this);
	var word_id = element.data('id');
	var word_meaning = element.data('meaning');
	var full_word = element.data('kanji');
	var already_clicked = element.data('clicked');
	
	if(already_clicked === false){
		add_word_to_stack(element, word_id, word_meaning, full_word);
	}else{
		remove_word_from_stack(element, word_id);
	}
});

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
	console.log(stack_preview_card);
};

var remove_word_from_stack = function(element, word_id){
	element.removeClass('add-word-button-clicked');
	element.html('Add <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>');
	$("#" + word_id).remove();
	document.getElementById('chosenwords' + word_id).remove();
	var already_clicked = element.data('clicked', false);	
};



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