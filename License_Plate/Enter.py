import pymongo
import cv2
from Garage import *
from bs4 import BeautifulSoup
from datetime import datetime
from ShapeDetection import detect_shape
from SendEmail import Send_Email
from Cost import *
from FrequentCustomer import Detect_Frequent
from Exit import Check_Exit
#take the current time
now=datetime.now()
now=now.strftime("%H%M")

#list
RemainSlot=[{'Slot':0}]
#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
#customer database : time_start,time_end,...
collection=database['garage']
collection2=database['customers']
collection3=database['docker']
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
    for f in collection.find({},{'user_id':1,'drivinglicensenumber':1,
                                 'startTime':1,'endTime':1,
                                 'email':1,'slot':1,
                                 'transId':1,'cost':1}).sort('transId',-1):
        #Check if there is a reservation
        if ((current_customer_plate==f['drivinglicensenumber'])and(f['cost']<0)):
            #Check if the customer is coming at the right time, 5 minutes before and 5 minutes later the reservation time
            time_start=int(now)-(int(f['startTime'][0])*1000+int(f['startTime'][1])*100+int(f['startTime'][3])*10+int(f['startTime'][4]))
            if (5>=time_start>=-5):
                currentshape=detect_shape(shapeimage)
                if currentshape=='car':
                    Slot=Assign_Slot('car')
                    #Update the slot
                    Old={"slot":f['slot']}
                    New={"$set":{"slot":Slot}}
                    collection.update_one(Old,New)
                    Send_Email(f['email'],str(Slot),f['startTime'],f['endTime'],f['cost'])
                    
                elif currentshape=='truck':
                    Slot=Assign_Slot('truck')                    
                    #update the slot
                    Old={"slot":f['slot']}
                    New={"$set":{"slot":Slot}}
                    collection.update_one(Old,New)
                    Send_Email(f['email'],str(Slot),f['startTime'],f['endTime'],f['cost'])
                if (collection3.count()==0):
                    RemainSlot[0]['Slot']=Slot_Left()
                    collection3.insert_many(RemainSlot)
                else:
                    for i in collection3.find():
                        Old={"Slot":i['Slot']}
                        New ={"$set":{"Slot":Slot_Left()}}
                        collection3.update_one(Old,New)
            else:
                print('Your time has expired')
            return True
        
    print('You havent registered yet')
    return False 
