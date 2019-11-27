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
collectionlicense=database['criminallicense']

current_customer_plate=input('license_plate')

for f in collectionlicense.find({},{'license_plate':1}):
    if (current_customer_plate==f['license_plate']):
        print('alert manager')
        break
    for i in collection.find({},{'License_plate':1,'Time_start':1}):
        if (current_customer_plate==i['License_plate']):
            print("Check")
            time_start=int(now)-(int(i['Time_start'][0])*1000+int(i['Time_start'][1])*100+int(i['Time_start'][3])*10+int(i['Time_end'][4]))
            if (5>=time_start>=-5):
                print('The car can go in')
            else:
                print('Please move out')
            break

