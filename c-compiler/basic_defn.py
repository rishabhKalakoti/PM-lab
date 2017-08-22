from variables import *

# check if statement is logical expression
def isLogicExp(text):
	text=text.strip()
	# <logicExp>--(<logicExp>)|<NOT><logicOp>|<logicExp><AND.OR><logicOp>|<compExp>
	if text.startswith("(") and text.endswith(")"):
		return isLogicExp(text[1:-1])
	elif text.startswith(logicOp_NOT):
		return isLogicExp(text[len(logicOp_NOT):])
	elif logicOp_lex in text:
		return isLogicExp(text[0:text.index(logicOp_lex)]) and isLogicExp(text[text.index(logicOp_lex)+len(logicOp_lex):])
	elif isCompExp(text):
		return True
	return False

def isCompExp(text):
	text=text.strip()
	# <compExp>--<compExp><comparisionOp><compExp>|(<compExp>)|<arithmeticExp>
	if text.startswith("(") and text.endswith(")"):
		return isCompExp(text[1:-1])
	elif compOp_lex in text:
		return isCompExp(text[0:text.index(compOp_lex)]) and isCompExp(text[text.index(compOp_lex)+len(compOp_lex):])
	elif isArithExp(text):
		return True
	return False

# check if statement is arithmetic expression
def isArithExp(text):
	text=text.strip()
	# <arithExp>--(<arithExp>)|<term><arithOp><arithExp>
	if text.startswith("(") and text.endswith(")"):
		return isArithExp(text[1:-1])
	elif arithOp_lex in text:
		return isArithExp(text[0:text.index(arithOp_lex)]) and isArithExp(text[text.index(arithOp_lex)+len(arithOp_lex):])
	elif isTerm(text):
		return True
	return False

# check if the term is right
def isTerm(text):
	text=text.strip()
	if text.startswith("(") and text.endswith(")"):
		return isTerm(text[1:-1])
	elif text.isnumeric():
		return True
	return False

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
	if not (not text[0]==None) and (text[0].isalpha() or text[0]=="_"):
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
