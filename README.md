# Project Name
## Overview
It's easy to imagine how hard simple tasks in life can become once we lose our vision. Well, Orbis reports **43 million people** globally live with blindness. For these people, out of Ranker's 14 most common problems they face when being blind, two of them involve money. Thus, we created an application to allow the visually impaired to identify money amounts. Users will use a phone app that classifies money bills and reads out money bill values.
## Interface
Our application is built with OpenCV and Python. To use the app, point the device camera towards a bill. Tap anywhere on the screen to classify the bill amount. The application will make an api call to our model and return the amount of money. It will then use Google Cloud's text-to-speech API to return an audio recording of the classification and return it to the user.
## Machine Learning

