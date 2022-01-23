<template>
<div>
<video id = 'cam'></video>
<canvas id="canvas"></canvas>
</div>
</template>

<script>
window.onload = function() {
var video = document.getElementById('cam');

video.style.display = 'none';

var canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var context = canvas.getContext('2d');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    const constraints = {
 "video": {
   "facingMode": 
      { "ideal": "environment" }
  }
};
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// say a message
function speak(text, callback) {
    var u = new SpeechSynthesisUtterance();
    u.text = text;
    u.lang = 'en-US';
 
    u.onend = function () {
        if (callback) {
            callback();
        }
    };
 
    u.onerror = function (e) {
        if (callback) {
            callback(e);
        }
    };
 
    speechSynthesis.speak(u);
}

context.rect(0, 0, 50, 50);
context.fillStyle = 'white';
context.fill();

context.drawImage(video, 0, 0, canvas.width, canvas.height);

canvas.addEventListener('touchend', function(ev) {

    console.log("Event");
    let imageData = canvas.toDataURL("image/jepg");

    var httpPost = new XMLHttpRequest();
    httpPost.open("POST", "http://172.105.103.43:5000/api/v0/classifyImage", true);
    httpPost.setRequestHeader("Content-Type", "application/json");
    httpPost.send(JSON.stringify({
        file: imageData
    }));

    httpPost.onload = () => {
        console.log(httpPost.responseText)

        speak(httpPost.responseText);

    }
}, false);

canvas.addEventListener ( "click", function ( ) {
                let imageData = canvas.toDataURL("image/jepg");

                context.rect(0, 0, 50, 50);

                var httpPost = new XMLHttpRequest();
                httpPost.open("POST", "http://172.105.103.43:5000/api/v0/classifyImage", true);
                httpPost.setRequestHeader("Content-Type", "application/json");
                httpPost.send(JSON.stringify({
                    file: imageData
                }));

                httpPost.onload = () => {
                    console.log(httpPost.responseText)

                    speak(httpPost.responseText);

                }

            } );


const runFunction = () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
}

var t=setInterval(runFunction,24/1000);


}

</script>