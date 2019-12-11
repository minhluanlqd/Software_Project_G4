import pymongo
from RealOnlineData import Update_Blacklisted
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collectionlicense=database['criminallicense']
Update_Blacklisted()
def Detect_Blacklisted(current_customer_plate):
    for f in collectionlicense.find({},{'license_plate':1}):
        if (str(current_customer_plate)==f['license_plate']):
            print('Alert Manager: Blacklisted car detected')
            return False
