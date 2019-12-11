def toASCII(myList):
	codedList = []
	for x in myList: codedList.append(ord(x))
	return codedList

def toEncryptedCode(myList):
	space = ' '
	nFile = open('n.txt')
	n = int(nFile.readline()) 
	nFile.close()
	eFile= open('e.txt')
	e = int(eFile.readline())
	eFile.close()

	linesList = []

	for x in myList:
		c = hex((x**e)%n)
		linesList.append(str(c).replace('0x', ''))
		linesList.append(space)
	return "".join(linesList)
	
def encrypt(theLine):
	brokenline = list(theLine)
	codedList = toASCII(brokenline)
	return toEncryptedCode(codedList)