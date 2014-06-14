// var chosenwords = [1,2,3,4];
// document.getElementById('chosenwords').value = chosenwords;

var filter = "grade";

var search = function(signal){
	
	$.ajax({
		url:'http://localhost:8000/profile/new-set/word-search',
		type:'GET',
		// dataType: 'json',
		data:{theorder: filter , csrfmiddlewaretoken: '{{ csrf_token }}'},
		success: function(data){
			
			data = JSON.parse(data);
			console.log("workeds");
			
			if (signal == ''){
				keyword = '';
			}else{
			keyword = document.getElementById('searchbox').value;
			}
			
			var foundflag = false;
			var content = "";
			
			if(keyword == ''){
				for(var i= 0; i<data.length; i++){
					
						content = content + "<div id = 'answercontainer' class = 'answerbox' >";
						content = content + "<div class = 'flipper'><div class = front>"; 
						content = content + "<div id = 'kanji'>" + data[i].fields.kanji_name + "</div>";
						content = content + "<div id = 'meaning'>" + data[i].fields.kanji_meaning + "</div>";
						content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
						content = content + "<button class = 'add-remove'>know it!</button>";
						content = content + "<button class = 'add-remove'>add</button>";
						content = content + "</div></div>"
						content = content + "<div class = 'back'>" + data[i].fields.kanji_name + "</div></div></div>";
						
					}
				document.getElementById('container').innerHTML = content;	
						
			}else{
				
				for(var i= 0; i<data.length; i++){
					
					if(data[i].fields.kanji_meaning.toLowerCase().indexOf(keyword.toLowerCase())!= -1||data[i].fields.kanji_name.indexOf(keyword)!=-1){
				
						content = content + "<div id = 'answercontainer' class = 'answerbox' onclick = 'clicked(this)'>";
						content = content + "<div class = 'flipper'><div class = front>"; 
						content = content + "<div id = 'kanji'>" + data[i].fields.kanji_name + "</div>";
						content = content + "<div id = 'meaning'>" + data[i].fields.kanji_meaning + "</div>";
						content = content + "<div id = 'grade'>" + data[i].fields.grade + "</div>";
						content = content + "<button class = 'add-remove'>know it!</button>";
						content = content + "<button class = 'add-remove'>add</button>";
						content = content + "</div></div>"
						content = content + "<div class = 'back'>" + data[i].fields.kanji_name + "</div></div></div>";
						foundflag = true;
					}
					
					if(foundflag == true){
						document.getElementById('container').innerHTML = content;
					}else{
						document.getElementById('container').innerHTML = "There are no matching results for your query: " + keyword ;
					}
						
					
					
				}
			}
				// document.getElementById('container').innerHTML = content;
			
			
		},
		failure: function(data){
			alert("Sorry got an error")
		}
	});
};


document.getElementById('strokes').onclick = function(){
	filter = "strokes";
	search('');
}

document.getElementById('gradefilter').onclick = function(){
	filter = "grade"
	search("yes");
}

document.getElementById('searchbox').onkeyup = function(){
	// filter = "grade"
	search("yes");
}

search('');
		
