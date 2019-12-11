import cv2
import numpy as np


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def Face_Recognition(image,template):
    #imagebackground
    image=cv2.imread(image)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    if (len(faces)>0):
        #image need to match
        template=cv2.imread('',0)#gray
    match=cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
    threshhold=0.8
    location=np.where(res>=threshhold)
    if (len(location)>0):
        print('Customer')
    else:
        print('Not our Customers')
    cv2.imshow('Match',image)
