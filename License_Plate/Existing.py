import pymongo
from datetime import datetime


#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['garage']
collection2=database['payment']
current_customer_plate=input('license_plate')

#list
newtransaction=[{'Username':'0','TransactionID':'0','Cost':0}]

#overtime cost
overtime=1
#take the current time
now=datetime.now()
now=now.strftime("%H%M")

#when the customer exits,the total cost will send to the blockchainpart
for i in collection.find({},{'Username':1,'License_plate':1,'Time_end':1}):
    if (current_customer_plate==i['License_plate']):
        time_actual_end=int(now)-(int(i['Time_end'][0])*1000+int(i['Time_end'][1])*100+int(i['Time_end'][3])*10+int(i['Time_end'][4]))
        print(time_actual_end)
        if (time_actual_end>5):
            overtime=(time_actual_end-5)*2
            print(overtime) #overtime price
            lot=collection2.count()
            newtransaction[0]['Username']=i['Username']
            newtransaction[0]['TransactionID']=str(lot+1)       
            newtransaction[0]['Cost']=overtime
            print(newtransaction[0])
            x=collection2.insert_many(newtransaction)
##

