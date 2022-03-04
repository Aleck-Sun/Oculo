import React, { useRef, useEffect } from 'react';
import './Camera.css';

const Camera = () => {
    const videoRef = useRef(null);
    const photoRef = useRef(null);
    const audioRef = useRef(null);

    // Get camera feed and play in video element
    const getVideo = () => {
        navigator.mediaDevices
            .getUserMedia({
                video: {
                    facingMode: "user",
                }
            })
            .then(stream => {
                let video = videoRef.current;
                video.srcObject = stream;
                video.play();
            })
            .catch(err => {
                console.log(err);
            });
    };

    const sendImage = async (imageFile) => {
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(imageFile)
        };

        const response = await fetch('http://localhost:5000/api/v0/classifyImage', options);
        const blob = await response.blob();
        var audioURL = URL.createObjectURL(blob);
        console.log(audioURL);
        playAudio(audioURL);
    };

    // Play returned audio file
    const playAudio = (audioFile) => {
        let audio = audioRef.current;
        audio.src = audioFile;
        audio.play();
    };

    // Takes a snapshot of video and classifies
    const getPhoto = () => {
        let video = videoRef.current;
        let photo = photoRef.current;
        photo.width = video.videoWidth;
        photo.height = video.videoHeight;

        try {
            photo.getContext('2d').drawImage(video, 0, 0, photo.width, photo.height);
            const dataURL = photo.toDataURL("image/png").split(",")[1];

            // Send dataURL to backend and get sound
            sendImage(dataURL);
        } catch (err) {
            console.log(err);
        }
    };

    useEffect(() => {
        getVideo();
    }, [videoRef]);

    return(
        <div className="camera-wrapper" onClick={getPhoto}>
            <video className="camera" ref={videoRef}></video>
            <canvas className="canvas" ref={photoRef}></canvas>
            <audio className="audio" ref={audioRef}></audio>
        </div>
    );
}

export default Camera;