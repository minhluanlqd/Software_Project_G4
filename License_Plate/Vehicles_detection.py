import cv2
import time
import os
# capture frames from a video
cap = cv2.VideoCapture('test.mp4')
 
#XML classifier
car_cascade = cv2.CascadeClassifier('cars.xml')
path='C:/Python Project/Parking Lot Garage/License_plate_picture'
start_time=time.time()
capture_duration=10
capture_extend=20
i=0
while True:
    
    ret, frames = cap.read()
    if (int(time.time()-start_time)<capture_duration):   
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cv2.imwrite(os.path.join(path,str(i)+'.png'),frames)  
        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        i=i+1               
    else:
        if (int(time.time()-start_time)<capture_extend):
            start_time=time.time()
   
    cv2.imshow('video2', frames)

    if cv2.waitKey(1) ==0 & 0xFF==ord('q'):
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
cap.release()
