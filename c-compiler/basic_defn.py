# remove elements from text stack at indices in list index
def removeExtra(index, text):
	while len(index)>0:
		text.pop(index.pop())
def showError(txt):
	print("")
	print("X"*25)
	print(txt)
	print("")
	exit(-1)

# function to check if the function or variable name is valid
def isValidName(text):
	# underscore, not at start
	# rest alphaNum or underscore
	if not text[0].isalnum():
		return False
	for i in range(len(text)):
		if  not (text[i].isalnum() or text[i]=='_'):
			return False
	return True 

# function to check funcition call validity
def isFileName(txt):
	txts=txt.split(".")
	for i in range(len(txts)):
		if(not isValidName(txts[i])):
			return 0
	return 1
