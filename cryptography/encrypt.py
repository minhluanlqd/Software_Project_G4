def toASCII(myList):
	codedList = []
	for x in myList: codedList.append(ord(x))
	return codedList

def toEncryptedFile(myList):
	space = ' '
	nFile = open('n.txt')
	n = int(nFile.readline())
	nFile.close()
	eFile= open('e.txt')
	e = int(eFile.readline())
	eFile.close()
	encryptedFile = open('encrypted_Data.txt', "w")
	for x in myList:
		c = hex((x**e)%n)
		encryptedFile.write(str(c).replace('0x', ''))
		encryptedFile.write(space)
	encryptedFile.close()
	return 'Done'
	
dataFile = open('Data.txt')
line = dataFile.read()
dataFile.close()
brokenline = list(line)
codedList = toASCII(brokenline)

print(toEncryptedFile(codedList))