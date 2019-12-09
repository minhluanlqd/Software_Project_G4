from block import Block 
from encrypt import *
from decrypt import * 


with open('ledger.txt', 'r') as ledgerFile: 
	ledgerdata = ledgerFile.readlines()
with open('hashtable.txt', 'r') as hashFile: 
	hashdata = hashFile.readlines()

blockChain = [Block.genesisBlock()]
if(len(ledgerdata) == 0):
	ledgerdata.insert(0, encrypt(str(0) + " " + str(0)) + '\n')
	hashdata.insert(0, blockChain[-1].hash + '\n')

with open('ledger.txt', 'w') as ledgerFile:
	ledgerFile.writelines(ledgerdata)
with open('hashtable.txt', 'w') as hashFile:
	hashFile.writelines(hashdata)


def buildBlocks():
	with open('ledger.txt', 'r') as ledgerFile: 
		ledgerdata = ledgerFile.readlines()
	with open('hashtable.txt', 'r') as hashFile: 
		hashdata = hashFile.readlines()

	for i in range(len(ledgerdata)):
		transaction = decrypt(ledgerdata[i].split()).split()
		if(i == 0):
			continue
		blockChain.append(Block(blockChain[-1].hash, int(transaction[0]), float(transaction[1]), i))
		if(blockChain[i].hash != hashdata[i].strip('\n')): 
			print("THE BLOCKCHAIN WAS TAMPERED WITH")
			break


def addBlock(transNum, userID, cost): 
	with open('ledger.txt', 'r') as ledgerFile: 
		ledgerdata = ledgerFile.readlines()
	with open('hashtable.txt', 'r') as hashFile: 
		hashdata = hashFile.readlines()

		if(len(ledgerdata) < (transNum+1)):
			blockChain.append(Block(blockChain[-1].hash, int(userID), float(cost), int(transNum))) 
			ledgerdata.insert(transNum, encrypt(str(userID) + " " + str(cost)) + '\n')
			hashdata.insert(transNum, blockChain[-1].hash + '\n')

	with open('ledger.txt', 'w') as ledgerFile:
		ledgerFile.writelines(ledgerdata)
	with open('hashtable.txt', 'w') as hashFile:
		hashFile.writelines(hashdata)


def getBalance(user):
	amount = 0
	data = open('ledger.txt').readlines()
	for i in range(len(data)): 
		if(int((decrypt(data[i].split()).split())[0]) == user):
			amount += float((decrypt(data[i].split()).split())[1])
	return amount


buildBlocks()
