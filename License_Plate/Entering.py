import pymongo
from datetime import datetime

#take the current time
now=datetime.now()
now=now.strftime("%H%M")
print(now)

#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['garage']
current_customer_plate=input('license_plate')
for i in collection.find({},{'License_plate':1,'Verification_ID':1,'Time_start':1,'Time_end':1,'Valid':1,'Time_end':1,'Car_entering':1,'Car_exiting':1,'Cost':1,'Overtime':1}):
    
    if ( time_end
    if (current_customer_plate==i['License_plate']):
        print("Check")
        time_end=int(now)-(int(i['Time_end'][0])*100+int(i['Time_end'][2])*10+int(i['Time_end'][3]))
        if (time_end5):
            overtime=(time_end-5)*2
            print('the cost')
##

