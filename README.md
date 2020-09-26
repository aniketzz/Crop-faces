# Crop-faces

This Script is used to Crop the face out from any image, video or camera feed. It uses face recognition API to detect the face.

Requirements:

face_recognition package
imutils
opencv

To install:
$pip install face_recognition imutils opencv-python==2.2.4

To test using live camera:
$python "crop face.py" -m camera -n xyz -d real

To test using image:
$python "crop face.py" -m image -n xyz -d real
