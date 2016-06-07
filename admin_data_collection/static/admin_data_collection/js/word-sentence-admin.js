$('input[type=submit]').on('click', function(event){
    event.preventDefault();
    //var form_element2 = $(this).parent();
    //var form_element = $('.formone').first()[0]
    //console.log(form_element);
    //var url = form_element2.attr('action');
    //var form_data = new FormData(form_element);
    //console.log(form_data)
    var id_number = $(this).attr('form-id');
    var form_element = $('#form_' + id_number);
    var url = form_element.attr('action');
    var form_data = new FormData(form_element[0]);
    console.log(form_data)
        
        
console.log(id_number);
    console.log(url);
    submitForm(url, form_data);
    
});

function submitForm(url, form_data){
      form_data.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
      type: "POST",
      url: url,
      data: form_data,
      success: function(data){
          console.log(data)   
      },
      processData: false,
      contentType: false,
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
