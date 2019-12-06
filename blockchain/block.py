import hashlib

class Block:
	def __init__(self, prevBlockHash, userID, cost, blockNumber):
		self.prevBlockHash = prevBlockHash
		self.userID = userID
		self.cost = cost
		self.blockNumber = blockNumber
		self.data = str(userID) + " " + str(cost)
		self.hash = self.getHash()

	@staticmethod
	def genesisBlock():
		return Block ("0", "0", "0", "0")

	def getHash(self):
		blockValue = (str(self.prevBlockHash) + str(self.data) + str(self.blockNumber)).encode() 
		hash = hashlib.sha256(blockValue).hexdigest().encode()
		return hash