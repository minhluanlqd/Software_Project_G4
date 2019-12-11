import pymongo
import cv2
from datetime import datetime
from Garage import *
from ShapeDetection import detect_shape
from SendEmail import Send_Email
from DetectBlacklisted import Detect_Blacklisted

#take the current time
now=datetime.now()
now=now.strftime("%H%M")
#list
RemainSlot=[{'Slot':0}]


def Check_Enter(current_customer_plate,image):
    #database
    connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
    database=connection['parkinglot']
    #customer database : time_start,time_end,...
    collection=database['garage']
    collection3=database['docker']
    if Detect_Blacklisted(current_customer_plate) is False:
        return False
    #If not blacklist car, compare the time start in the database to check
    for f in collection.find({},{'user_id':1,'drivinglicensenumber':1,
                                 'startTime':1,'endTime':1,
                                 'email':1,'slot':1,
                                 'transId':1,'cost':1}).sort('transId',-1):
        #Check if there is a reservation
        if ((current_customer_plate==f['drivinglicensenumber']) and (f['slot']==1)):
            
            #Check if it is reservation or cancelation
            if (f['cost']<0):
            #Check if the customer is coming at the right time, 5 minutes before and 5 minutes later the reservation time
                time_start=int(now)-(int(f['startTime'][0])*1000+int(f['startTime'][1])*100+int(f['startTime'][3])*10+int(f['startTime'][4]))
                print(time_start)
                if (5>=time_start>=-5):
                    currentshape=detect_shape(image)
                    if currentshape=='car':
                        Slot=Assign_Slot('car')
                        #Update the slot
                        Old={"slot":f['slot']}
                        New={"$set":{"slot":Slot}}
                        
                    
                    elif currentshape=='truck':
                        Slot=Assign_Slot('truck')                    
                        #update the slot
                        Old={"slot":f['slot']}
                        New={"$set":{"slot":Slot}}
                    collection.update_one(Old,New)
                    Send_Email(f['email'],str(Slot),f['startTime'],f['endTime'],f['cost'])
                    print('Gmail has been sent')
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
            print('Your cancellation have been canceled')
            return False
        
    print('You havent registered yet')
    return False 
