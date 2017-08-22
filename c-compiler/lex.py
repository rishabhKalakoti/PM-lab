from variables import *

# trying to add a little of the lexical analyzer component...

def theLexer(text):
	for i in range(len(text)):
		# logical operators
		x=logicOp_lex
		text[i]=x.join(text[i].split("&&"))
		text[i]=x.join(text[i].split("||"))
		x=logicOp_NOT
		text[i]=x.join(text[i].split("!"))
		# comparision operators
		x=compOp_lex
		for compOp in comparisionOp:
			text[i]=x.join(text[i].split(compOp))
		# arithmetic operators
		x=arithOp_lex
		for arithOp in arithmeticOp:
			text[i]=x.join(text[i].split(arithOp))
		
		# init statement
		if text[i].split()
	return text
