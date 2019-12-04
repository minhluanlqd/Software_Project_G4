import pymongo
import cv2
import os
import requests
import base64
import json
from bs4 import BeautifulSoup
from datetime import datetime
from ShapeDetection import detect_shape


i=0
#test camera
cap = cv2.VideoCapture('test.mp4')

#take the current time
now=datetime.now()
now=now.strftime("%H%M")

#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
#customer database : time_start,time_end,...
collection=database['garage']
#criminal license database
collectionlicense=database['criminallicense']

#XML classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

#ALPR
SECRET_KEY = 'sk_8d7c25a2ea0f1d3b289715a9'
url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
#Picture path
path='C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/Images/'




while True:
    
    ret, frames = cap.read() 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
         
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    cv2.imwrite(os.path.join(path,str(i)+'.png'),frames)  
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
    image=path+str(i)+'.png'
    #Detect license_plate
    with open(image, 'rb') as image_file:
        #Detect License 
        img_base64 = base64.b64encode(image_file.read())
        r = requests.post(url, data = img_base64)
    
    
    #Take the current license plate
    current_license_plate=r.json()
    current_license_plate=current_license_plate["results"][0]['plate']
    print(current_license_plate)

    #Take the current image path to detech the shape of the car 
    shapeimage=cv2.imread(image)
    
    #Compare with blacklist car   
    for f in collectionlicense.find({},{'license_plate':1}):
        if (str(current_license_plate)==f['license_plate']):
            print('alert manager')
            break
    #If not blacklist car, compare the time start in the database to check 
    for f in collection.find({},{'License_plate':1,'Time_start':1}):
        #Check if there is a reservation
        if (current_license_plate==f['License_plate']):
            #Check if the customer is coming at the right time, 5 minutes before and 5 minutes later the reservation time
            time_start=int(now)-(int(f['Time_start'][0])*1000+int(f['Time_start'][1])*100+int(f['Time_start'][3])*10+int(f['Time_start'][4]))
            if (5>=time_start>=-5):
                currentshape=detect_shape(shapeimage)
                if currentshape=='car':
                    print('car')
                elif currentshape=='truck':
                    print('truck')
            else:
                print('Please move out')
                    
    i=i+1
    
    cv2.imshow('video2', frames)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
cap.release()
