#!/usr/bin/python

import requests
import base64
import json
import os



#CLOUD API 
SECRET_KEY = 'sk_f8083dc6aac647e1b7eff780'
url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)



#Take license function
def Take_License(image):
    
    with open(image, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())
        r = requests.post(url, data = img_base64)

    #Take the information from detecting
    current_customer_plate=r.json()  
    #ALPR 
    try:
        current_customer_plate=current_customer_plate["results"][0]['plate']
    except:
        print('There is no customer who is coming in')
        current_customer_plate=None
    return current_customer_plate

