import React, { useState, useEffect } from "react";
import Camera from '../Camera/Camera';
import logo from '../../Images/logo.png';
import './SplashScreen.css';

const SplashScreen = () => {
    const [openCamera, setOpenCamera] = useState("");

    useEffect(() => {
        setTimeout(() => {
            setOpenCamera("hidden");
        }, 3000)
    }, [])
    
    return(
        <>
            <div className={"wrapper " + openCamera}></div>
            <img src={logo} className={"logo " + openCamera + "-image"}></img>
            {openCamera != "" ? <Camera /> : null}
        </>
    );
}

export default SplashScreen;