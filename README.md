# Oculo
Oculo is a cross-platform application built to help the visually impaired identify money amounts and have them read out loud for them. The app can be accessed on the web [here](https://oculo.netlify.app/) and mobile [here.]()
<br>
<br>
**Note:** The API takes ~1 min for the first classification and afterwards should take about 1-5 sec for each classification

## Demo
> **Devpost:** https://devpost.com/software/oculo<br/>
> **Video Demo:** INSERT VIDEO LINK LATER

**INSERT GIF HERE LATER**

## Inspiration
During a conversation with a US friend, we found out that US bills don't have brailles, unlike Canada. We wondered how in the world blind people in the US deal with money. So we did some research and found Orbis reports **43 million people** globally live with blindness. For these people, out of Ranker's 14 most common problems they face when being blind, two of them involve money. Thus, we created Oculo to help the visually impaired identify money amounts.

## How it works
The client is built to be super straightforward and simple for blind people to use. Users just have to point the device camera towards a bill, then tap anywhere on the screen to classify the bill amount. The application will make an api call to our backend. The backend identifies the bill amount using our model, then uses Google Cloud's text-to-speech API to return the amount of money in an audio format. The client receives the audio and plays it to the user.

Our app also supports changing camera modes. Users can double click anywhere to change from rear to front camera and vice versa. When changing, the app plays an audio prompt to let the user know which camera mode they are in.

**Technology:**<br/>
The frontend is built with React and Kotlin. The backend is built with Flask and Google Cloud. The model was built using PyTorch and data was collected using Selenium and Microsoft Azure Bing API.

## API
Our API will return an audio blob of the classification of the base64 image sent to it through a post request
```http
POST https://oculo.herokuapp.com/api/v0/classifyImage
```
| Response | Post Body |
| :--- | :--- |
| `blob` | `base64 image` |
