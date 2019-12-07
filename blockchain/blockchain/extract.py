from blockchain import *

#addBlock(transaction number, user number, cost)
#getBalance(user number)

addBlock(1, 5, 100)
print("The Balance of this user is: $%d" %getBalance(5))

