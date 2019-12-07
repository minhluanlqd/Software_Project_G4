def toDec(theList):
	finalList = []
	
	for x in theList: 
		if(x == ''):
			theList.remove(x)
		else:
			finalList.append(int(x,16)) 
	return finalList

def toDecryptedFile(myList):
	dFile = open('d.txt')
	d = int(dFile.readline())
	dFile.close()
	nFile = open ('n.txt')
	n = int(nFile.readline())
	nFile.close()

	linesList = []

	for c in myList:
		m = chr((c**d)%n)
		linesList.append(str(m))
	return "".join(linesList)

def decrypt(theList):
	return toDecryptedFile(toDec(theList))