$('input[type=submit]').on('click', function(event){
    event.preventDefault();
    var form_element2 = $(this).parent();
    var form_element = $('.formone').first()[0]
    console.log(form_element);
    var url = form_element2.attr('action');
    var form_data = new FormData(form_element);
    //var form_data = 1;
    console.log(form_data)

    submitForm(url, form_data);
    
});

function submitForm(url, form_data){
    word_id = 4;
      form_data.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
      type: "POST",
      url: url,
      //data: { word_id:'1', csrfmiddlewaretoken: csrftoken},
      //data:{word_id: form_data, csrfmiddlewaretoken: csrftoken},
      //data: word_id,
      //data: {word_id: form_data, csrfmiddlewaretoken: csrftoken},
      data: form_data,
      success: function(data){
          console.log(data)   
      },
      processData: false,
      contentType: false,
      //contentType: 'multipart/form-data',
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
