# SustainLens
- Alexander Zhong, Diego Nisperos for Learn It Global Hackathon

## Inspiration
We believe sustainability starts within us. Not organization, big companies or corporations. We all have the power to solve sustainable issues. It all begins with every one of us taking little steps towards tackling these issues. Although each one of us may seem to contribute little, together, we can make something beautiful happen. SustainLens is the support to this movement.  

## What it does
SustainLens an application that has a camera embedded with AI. At its current state, with a simple picture upload, it uses CNN models trained based on data that we have collected to classify whether items are recyclable or not. In future updates, we hope to collect more data and be able to identify more complex labels such as garbage, recyclable, food waste, and etc. 

## How we built it
Starting off with CNN models, it was constructed using a neural network API, Keras, from tensorflow library. Then, we collected data from free stock images of recyclable material as well as non-recyclable material for training the model. After spending hours learning and building the architecture of our neural network model, we trained it with the data and adjusted the architecture and tuned the parameters to prevent overfitting or underfitting. 

For the user interface aspect, we opted to utilize HTML, CSS, and Python's lightweight framework, Flask, for users to upload images and get displayed results from our model. Our webpage features a navigation bar at the top, enabling users to access the upload page conveniently. As part of our ongoing development, we plan to integrate a new feature into the navigation bar, allowing users to utilize their device cameras to capture directly and verify whether an object is recyclable or not. 

## Challenges we ran into
BUILDING A CNN NETWORK IS HARD! But it was worth it! 😀It is our very first hackathon project using technologies in our roles that we both were quite unfamiliar with. There were many times where we thought that we aimed too high for what we could do but after sleepless nights and hours in the library, we managed to pull together a project. 

## Accomplishments that we're proud of
Although having no experience in the roles we put ourselves in, we managed to develop and train a CNN model capable of classifying recyclable and non-recyclable items based on image input as well as creating a user-friendly web application that allows users to easily upload images and receive real-time classification results. 

## What's next for SustainLens
Our plan in the far future is to incorporate our app within Apple’s vision pro to have a live interaction where AI models can identify live real-time sustainability tips or classifications of where to throw items. 

  

