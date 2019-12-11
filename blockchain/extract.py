import pymongo
from blockchain import *

connection = pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
dataBase = connection['parkinglot']
data = dataBase['garage']

for x in data.find({},{"transId" : 1, "user_id" : 1, "cost" : 1}):
	addBlock(int(x['transId']), int(x['user_id']), float(x['cost']))

i = input("What user's balance do you need?: ")
print("The Balance of User %d is: $%.2f" %(i, getBalance(i)))

print("\nDATA (ENCRYPTED): ")
print(open('ledger.txt','r').read())
print("\nHASHES: ")
print(open('hashtable.txt', 'r').read())
