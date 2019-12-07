import pymongo
import cv2
from Garage import *
from bs4 import BeautifulSoup
from datetime import datetime
from ShapeDetection import detect_shape
from SendEmailEnters import Send_Email_Enter
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

def Check_Enter(current_customer_plate,image):
    
    #Take the current image path to detech the shape of the car 
    shapeimage=cv2.imread(image)
    #Compare with blacklist car
    for f in collectionlicense.find({},{'license_plate':1}):
        if (str(current_customer_plate)==f['license_plate']):
            print('Alert Manager:Blacklisted car detected')
            return False
    #If not blacklist car, compare the time start in the database to check
    for f in collection.find({},{'License_plate':1,'Time_start':1,'Time_end':1,'Email':1,
                                 'Slot':1,'ID':1}).sort('ID',-1):
        #Check if there is a reservation
        if (current_customer_plate==f['License_plate']):
            #Check if the customer is coming at the right time, 5 minutes before and 5 minutes later the reservation time
            time_start=int(now)-(int(f['Time_start'][0])*1000+int(f['Time_start'][1])*100+int(f['Time_start'][3])*10+int(f['Time_start'][4]))
            if (5>=time_start>=-5):
                currentshape=detect_shape(shapeimage)
                print (currentshape)
                if currentshape=='car':
                    Slot=Assign_Slot('car')
                    OldSlot={"Slot":"1"}
                    NewSlot={"$set":{"Slot":str(Slot)}}
                    collection.update_one(OldSlot,NewSlot)
                    Send_Email_Enter(f['Email'],str(Slot),f['Time_start'],f['Time_end'])
                elif currentshape=='truck':
                    Slot=Assign_Slot('truck')
            else:
                print('Your time has expired')
            return True
        
    print('You havent registered yet')
    return False 
    
