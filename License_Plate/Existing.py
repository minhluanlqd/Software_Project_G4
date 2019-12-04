import pymongo
from datetime import datetime
from FrequentCustomer import Detect_Frequent

#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['garage']
collection2=database['payment']

#list
newtransaction=[{'Username':'0','TransactionID':'0','Cost':0}]
myquery={}

#overtime cost
overtime=1

#take max
maxID=1
#take the current time
now=datetime.now()
now=now.strftime("%H%M")

#when the customer exits,the total cost will send to the blockchainpart
while True:
    current_customer_plate=input('license_plate')
    for i in collection.find({},{'Username':1,'License_plate':1,'Time_end':1,'ID':1}).sort('ID',-1):
        if (current_customer_plate==i['License_plate']):
            time_actual_end=int(now)-(int(i['Time_end'][0])*1000+int(i['Time_end'][1])*100+int(i['Time_end'][3])*10+int(i['Time_end'][4]))
            print(time_actual_end)
            if (time_actual_end>5):
                #reduce the cost depends on the account
                reduction=Detect_Frequent(current_customer_plate)
                #calculate the overtime price
                overtime=(time_actual_end-5)*2
                print(overtime) #overtime price
                lot=collection2.count()
                newtransaction[0]['Username']=i['Username']
                for lastID in collection2.find({},{'TransactionID':1}):
                    if int(lastID['TransactionID']) > maxID:
                        maxID=int(lastID['TransactionID'])
                newtransaction[0]['TransactionID']=str(maxID+1)       
                newtransaction[0]['Cost']=overtime-overtime*reduction
                print(newtransaction[0])
                #x=collection2.insert_many(newtransaction)
            break


