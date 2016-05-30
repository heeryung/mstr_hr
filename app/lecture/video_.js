
//video play

//vide


//video ended
var vid = document.getElementById("myVideo");
vid.onended = function() {
	alert("The video has ended");
	return video_ended = true;
};

// record beginning time, record ending time
= begin_time
var pending_time = current_time -


// record the percent of video watching
//Get current percent complete. You may want to check for 95%+ rather than 100%.
setInterval(function(){
    percentComplete = player.currentTime/player.duration;
}, 300); 



//window onblur
window.onblur = function() {
   //do something here...
};

//