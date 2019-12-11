#take data from an internet
import requests
from bs4 import BeautifulSoup
import pymongo

items=[]
license_plate=[]

# a database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['criminallicense']
# Collect and parse first page
page = requests.get('https://www.stolencar.com/Report/Search')
soup = BeautifulSoup(page.content, 'html.parser')
Car_stolen_list=soup.find_all(class_='col-sm-6')
def Update_Blacklisted(): 
    if (collection.count()==0): #if the database is having nothing
        for car in Car_stolen_list[1:]:
            c=car.get_text()
            items=c.split()
            if ((items[4]=='Plate:')):
                license_plate.append(items[5])
            elif (items[4]=='TEMPORARY'):
                pass        
            else:
                if (len(items[4])<5):
                    license_plate.append(items[4]+items[5])
                else:
                    license_plate.append(items[4])
        k=len(license_plate)
        final_license=[]
        #delete the duplicate
        for i in range(k):
            if license_plate[i] not in final_license:
                final_license.append(license_plate[i])
        #insert into the database
        for i in range(len(final_license)):
            collection.insert_one({'license_plate':final_license[i]})
    else: #update a new one, if the new one is like the data in the databse,not updating
        for car in Car_stolen_list[1:2]:
            c=car.get_text()
            items=c.split()
            if ((items[4]=='Plate:')):
                license_plate.append(items[5])
            elif (items[4]=='TEMPORARY'):
                pass        
            else:
                if (len(items[4])<5):
                    license_plate.append(items[4]+items[5])
                else:
                    license_plate.append(items[4])
        #compare if the database is having the new one or not           
        license_plate_db=collection.find()
        h=0
   
        for i in collection.find({},{'_id':0,'license_plate':1}):
            if license_plate[0]==i['license_plate']:
                h=h+1
                if h>0:
                    break
        if h==0:
            collection.insert_one({'license_plate':license_plate[0]})
      


