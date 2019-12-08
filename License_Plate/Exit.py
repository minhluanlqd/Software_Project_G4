import pymongo
from datetime import datetime
from FrequentCustomer import Detect_Frequent
from Garage import *
#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['garage']

#list
newtransaction=[{'UserID':'0','transId':'0','Cost':0}]
myquery={}

#overtime cost
overtime=1

#take max
maxID=1
#take the current time
now=datetime.now()
now=now.strftime("%H%M")

#when the customer exits,the total cost will send to the blockchainpart
def Check_Exit(current_customer_plate):
    for i in collection.find({},{'user_id':1,'drivinglicensenumber':1,
                                 'endTime':1,'slot':1,'cost':1,
                                 'transId':1}).sort('transId',-1):
        if (current_customer_plate==i['drivinglicensenumber']):
            time_actual_end=int(now)-(int(i['endTime'][0])*1000+int(i['endTime'][1])*100+int(i['endTime'][3])*10+int(i['endTime'][4]))
            if (time_actual_end>5):
                #reduce the cost depends on the account
                reduction=Detect_Frequent(current_customer_plate)
                #calculate the overtime price
                overtime=-(time_actual_end-5)*1.5
                OldCost={"cost":i['cost']}
                NewCost={"$set":{"cost":overtime+i['cost']}}
                x=collection.update_one(OldCost,NewCost)
            Release_Slot(i['slot'])
            OldSlot={"Slot":i['slot']}
            NewSlot={"$set":{"slot":1}}
            collection.update_one(OldSlot,NewSlot)
            print(Is_Empty_Slot(103))
            break
        

