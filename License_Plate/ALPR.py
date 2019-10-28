#!/usr/bin/python

import requests
import base64
import json
import os

#customer database
mylist=os.listdir('C:/openalpr/samples/File')
for i in mylist:
    IMAGE_FILE = 'C:/openalpr/samples/File/'+str(i)
    SECRET_KEY = 'sk_8d7c25a2ea0f1d3b289715a9'

    with open(IMAGE_FILE, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)
    #results
    h=r.json()
    print(h["results"][0]['plate'])

#take licesne and put them into two database

#crime database
