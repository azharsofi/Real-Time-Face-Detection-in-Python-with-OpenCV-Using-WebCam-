#import open cv library
import cv2
from random import randrange as r
#dataset load
trainedData=cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

#start webcam
webcam=cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)
while True:
 success,img=webcam.read()
 #convert to gray
 grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 #detect faces
 facecoordinates=trainedData.detectMultiScale(grayimg)
 for x,y,w,h in facecoordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(r(0,265),r(0,265),r(0,265)),2)
 #display image
 cv2.imshow('window',img)
 key=cv2.waitKey(1)
 if(key==113 or key==81):
  break;
webcam.release()
 
 







print('end of')