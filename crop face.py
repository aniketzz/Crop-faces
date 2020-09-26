#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aniket
#
# Created:     09-07-2020
# Copyright:   (c) aniket 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import face_recognition
import imutils
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mode", help="mode to capture data \"camera\" or \"image\"", default = "camera")
ap.add_argument("-n", "--name", help="enter the prefix name for the data", required = True)
ap.add_argument("-d", "--data", help="fake or real data", required = True)
args = vars(ap.parse_args())

def img_directory():
    path = 'data'
    if args['data'] == 'real':
        save_path = "test1"
    else:
        save_path = "test2"
    img_dir = sorted(os.listdir(path))
    count = 0
    for i in img_dir:
        frame = cv2.imread(path + i)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=512)
        r = frame.shape[1] / float(rgb.shape[1])
        boxes = face_recognition.face_locations(rgb,model="cnn")
        #print(len(boxes))
        if len(boxes) != 0:
            for (top, right, bottom, left)in boxes:
                # rescale the face coordinates
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                #print(top,bottom,left,right)
                new = frame[top:bottom,left:right]
                cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
                cv2.imwrite(save_path+args["name"]+str(count)+".jpg", new)
                count+=1
                cv2.imshow("img",frame)
                cv2.waitKey(0)

def camera():
    count = 0
    if args['data'] == 'real':
        save_path = "test1/"
    else:
        save_path = "test2"

    vidcap = cv2.VideoCapture('D:/tensorgo/antispoofing/aniket_fake.mp4')
    success,frame = vidcap.read()
    while success or count%5==0:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=512)
        r = frame.shape[1] / float(rgb.shape[1])
        boxes = face_recognition.face_locations(rgb,model="cnn")
        #print(len(boxes))
        if len(boxes) != 0:
            for (top, right, bottom, left)in boxes:
                # rescale the face coordinates
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                #print(top,bottom,left,right)
                new = frame[top:bottom,left:right]
                #cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
                cv2.imwrite(save_path+args["name"]+str(count)+".jpg", new)
                #print(args["name"]+str(count)+".jpg")
                count+=1


if args["mode"] == "image":
    img_directory()
    print("[Info]: Done!")
    cv2.destroyAllWindows()

elif args["mode"] == "camera":
    camera()
    print("[Info]: Done!")

else:
    print("Plese select either \'camera\' or \'image\' mode.")