var timezone_offset = (function(){
	var x = new Date();
	console.log(x.getTimezoneOffset())
	var currentTimeZoneOffsetInHours = x.getTimezoneOffset()/60
	return currentTimeZoneOffsetInHours
})();


(function(object_id, increase_level){
	user_name = document.getElementById('user-name').value;
	$.ajax({
		
		url:'/profile/' + user_name + '/update-words-practiced-today',
		type:'GET',
		data:{ csrfmiddlewaretoken: csrftoken, timezone_offset:timezone_offset},
		success: function(data){
			$('#test .big-number').html(data);
		}, 
		failure: function(data){
			alert("Sorry got an error on the AJAX")
		}
	});	
})()


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