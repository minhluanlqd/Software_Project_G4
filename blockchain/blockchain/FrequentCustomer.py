import pymongo
from datetime import datetime

def Detect_Frequent(current_license):
    #database
    costreduction=0
    number=0
    connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
    database=connection['parkinglot']
    collection=database['garage']
    for i in collection.find({},{'License_plate':1}):
        if current_license==i['License_plate']:
            number=number+1
    if (number>=3):
        print('Gold')
        costreduction=0.1
        return costreduction
    elif (3>number>=2):
        print('Silver')
        costreduction=0.05
        return costreduction
    else:
        return costreduction

