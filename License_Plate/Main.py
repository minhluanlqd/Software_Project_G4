import cv2
import time
import os
import requests
import base64
import json
from bs4 import BeautifulSoup

#holding criminal license plate
items=[]
license_plate=[]

# capture frames from a video
cap = cv2.VideoCapture('test.mp4')
 
#XML classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

#picture_path
path='C:/Python Project/Parking Lot Garage/License_plate_picture/'

#ALPR
SECRET_KEY = 'sk_8d7c25a2ea0f1d3b289715a9'
url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)

#time entering
start_time=time.time()
capture_duration=10
capture_extend=20
i=0

#taking the missing car from the internet
page = requests.get('https://www.stolencar.com/Report/Search')
soup = BeautifulSoup(page.content, 'html.parser')
Car_stolen_list=soup.find_all(class_='col-sm-6')
for car in Car_stolen_list[1:]:
    c=car.get_text()
    items=c.split()
    if ((items[4]=='Plate:')):
        license_plate.append(items[5])
    elif (items[4]=='TEMPORARY'):
        pass        
    else:
        license_plate.append(items[4])
print (license_plate)

#take current license plate
while True:
    
    ret, frames = cap.read()
    if (int(time.time()-start_time)<capture_duration):   
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
         
        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cv2.imwrite(os.path.join(path,str(i)+'.png'),frames)  
        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        image=path+str(i)+'.png'
        with open(image, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())
            r = requests.post(url, data = img_base64)

        #print current license plate
        h=r.json()
        print(h["results"][0]['plate'])

        #comparing license plate
        for i in range(len(license_plate)):
            if (license_plate[i]==h["results"][0]['plate']):
                print('Criminal')
            else:
                pass
        print('Not criminal')    
        
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
