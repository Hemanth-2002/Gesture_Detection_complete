Description:

Gesture recognition becomes popular in recent years since it can play an essential role in non-verbal communication, emotion analysis as well as human-computer interaction. The research task is to detect hand gestures in raw news videos which are streams of RGB images. I propose a Transformer and keypoints-based pose tracking system and a Transformer and keypoints-based gesture detector to fulfill this task. This structure is composed of a keypoints extractor, a person tracker, and a gesture detector. The mission has three main parts, the first part is to track people in temporal space. In the second part, for each person, we use their hand keypoints features in temporal space to construct several keypoints sequences. The third part is to use these sequences to make predictions of the existence of gestures. I believe that for gesture detection tasks, both spatial and temporal information is important. So that is why we use the Transformer which can take into account the local information of hand keypoints in one frame to capture the shape information and it values also the relationship of keypoints in different frames that is the global information refer to the motion.

The dataset for our project is available at https://chalearnlap.cvc.uab.cat/dataset/22/description/. I have worked with ICPR 16 dataset to train the gesture detection model.

In this project i managed to get the keypoints of a given jpeg file.The below images represents the work that i have done.

Input image of type jpeg or png:

![test1](https://user-images.githubusercontent.com/57759564/147106305-07e80179-dfaa-44e4-bff7-8d8935e154ee.jpg)



Input image along with keypoints:

![demo](https://user-images.githubusercontent.com/57759564/147197436-1f95a43c-3151-4b01-8abc-83b0557ada71.png)



For finding the keypoints of an image file i directly ran the _body_from_image.py. The output can be seen in the above image.
The model can also mark the keypoints for a video file this can be achieved by using the following commands:

-Windows
bin\OpenPoseDemo.exe --video examples\media\video.avi

-Ubuntu
./build/examples/openpose/openpose.bin

A json file can be produced using the image containing keypoints.The json file has the keypoints information.
The json file can be loaded into the evaluate.py which gives the output containing gesture detected or not detected.

I have applied the model on images and videos to find the keypoints of a file. I am yet to load the json file into the evaluate.py.
