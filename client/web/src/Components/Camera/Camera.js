import React, { useRef, useEffect, useState } from 'react';
import rearPrompt from '../../Images/rearmode.mp3';
import frontPrompt from '../../Images/frontmode.mp3';
import './Camera.css';

let clicks = 0;
const Camera = () => {
    const videoRef = useRef(null);
    const photoRef = useRef(null);
    const audioRef = useRef(null);
    const [facingMode, setFacingMode] = useState("user");

    // Get camera feed and play in video element
    const getVideo = () => {
        navigator.mediaDevices
            .getUserMedia({
                video: {
                    facingMode: facingMode,
                }
            })
            .then(stream => {
                let video = videoRef.current;
                video.srcObject = stream;
                video.play();

                // Audio prompt for camera facingmode
                const prompt = facingMode == "user" ? frontPrompt : rearPrompt;
                playAudio(prompt);
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

        const response = await fetch('https://oculo.herokuapp.com/api/v0/classifyImage', options);
        const blob = await response.blob();
        var audioURL = URL.createObjectURL(blob);
        playAudio(audioURL);
    };

    // Play returned audio file
    const playAudio = (audioFile) => {
        let audio = audioRef.current;
        audio.src = audioFile;
        audio.play();
    };

    const getPhoto = () => {
        // Switch camera angle
        if (clicks === 2) {
            const newMode = facingMode == "user" ? "environment" : "user";
            setFacingMode(newMode);
        } else if (clicks == 1) {
            // Takes a snapshot of video and classifies
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
        clicks = 0;
    };

    useEffect(() => {
        getVideo();
    }, [facingMode]);

    return(
        <div className="camera-wrapper" onClick={() => {
                clicks += 1;
                setTimeout(getPhoto, 500);
            }
        }>
            <video className="camera" ref={videoRef}></video>
            <canvas className="canvas" ref={photoRef}></canvas>
            <audio className="audio" ref={audioRef}></audio>
        </div>
    );
}

export default Camera;