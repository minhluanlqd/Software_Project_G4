import pymongo
from datetime import datetime
from FrequentCustomer import Detect_Frequent
from Garage import *

#when the customer exits,the total cost will send to the blockchainpart
def Check_Exit(current_customer_plate):
    #database
    connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
    database=connection['parkinglot']
    collection=database['garage']
    collection2=database['UserCount']
    #list
    newtransaction=[{'startTime':'0','endTime':'0',
                     'makeRes':'Create Reservation',
                     'user_id':'0','email':'0',
                     'drivinglicensenumber':'0',
                     'slot':'0','cost':0,
                     'transId':'0'
                     }]
    myquery={}

    #overtime cost
    overtime=1

    #take the current time
    now=datetime.now()
    now=now.strftime("%H%M")
    for i in collection.find({},{'user_id':1,'drivinglicensenumber':1,
                                 'startTime':1,'makeRes':1,'email':1,
                                 'endTime':1,'slot':1,'cost':1,
                                 'transId':1}).sort('transId',-1):
        if ((current_customer_plate==i['drivinglicensenumber']) and (i['slot']!=1)):
            time_actual_end=int(now)-(int(i['endTime'][0])*1000+int(i['endTime'][1])*100+int(i['endTime'][3])*10+int(i['endTime'][4]))
            time_start=int(now)-(int(i['startTime'][0])*1000+int(i['startTime'][1])*100+int(i['startTime'][3])*10+int(i['startTime'][4]))
            if (time_actual_end>5):
                #reduce the cost depends on the account
                reduction=Detect_Frequent(current_customer_plate)
                #calculate the overtime price
                overtime=(time_actual_end-5)*1.5
                overtime=-(overtime-overtime*reduction)
                newtransaction[0]['user_id']=i['user_id']
                newtransaction[0]['drivinglicensenumber']=i['drivinglicensenumber']
                newtransaction[0]['startTime']=i['startTime']
                newtransaction[0]['email']=i['email']
                newtransaction[0]['endTime']=i['endTime']
                newtransaction[0]['slot']=1
                newtransaction[0]['cost']=overtime
                for f in collection2.find():
                    newtransaction[0]['transId']=f['transCount']+1
                    OldTransaction={"transCount":f['transCount']}
                    NewTransaction={"$set":{"transCount":f['transCount']+1}}
                    collection2.update_one(OldTransaction,NewTransaction)
                collection.insert_many(newtransaction)
                Release_Slot(i['slot'])
                OldSlot={"slot":i["slot"]}
                NewSlot={"$set":{"slot":1}}
                collection.update_one(OldSlot,NewSlot)
                
                print('You have successfully exit')
            elif time_start>0:
                Release_Slot(i['slot'])
                OldSlot={"slot":i["slot"]}
                NewSlot={"$set":{"slot":1}}
                collection.update_one(OldSlot,NewSlot)
                print('You have successfully exit')
            return True
    print('You havent entered the parking lot')
    return False
Check_Exit('L29HMY')        

