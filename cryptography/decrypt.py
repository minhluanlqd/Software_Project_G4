def toList():
	cList = []
	cFile = open('encrypted_Data.txt')
	cBreak = list(cFile.readline().split(" "))
	for x in cBreak: 
		if(x == ''):
			cBreak.remove(x)
		else:
			cList.append(int(x,16))
	cFile.close()
	return cList

def toDecryptedFile(myList):
	dFile = open('d.txt')
	d = int(dFile.readline())
	dFile.close()
	nFile = open ('n.txt')
	n = int(nFile.readline())
	nFile.close()
	decryptedFile = open('decrypted_Data.txt', "w")
	for c in myList:
		m = chr((c**d)%n)
		decryptedFile.write(str(m))
	decryptedFile.close()
	return 'Done'

print(toDecryptedFile(toList()))