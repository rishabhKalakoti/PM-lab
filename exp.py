import re

# input 
print("input the expression")
exp=str(input("> "))
# remove spaces
exp = ''.join(exp.split())
length=len(exp)

# solve function
def solve(op1, op2, opn):
	if(opn == '+'):
		return op1+op2
	elif(opn == '-'):
		return op1-op2
	elif(opn == '*'):
		return op1*op2
	elif(opn == '/'):
		if(op2==0):
			exit("Division by 0 not possible")
		return op1/op2

# variables initialisation
oPtr=-1
oStack = []
vPtr=-1
vStack = []

# ********************************
# push all the values up the stacks
# ********************************
# operator stack
i=0
while i<length:
	if exp[i]=='+' or exp[i]=='-':
		oStack.append(exp[i])
	if exp[i]=='*' or exp[i]=='/':
		oStack.append(exp[i])
	i=i+1
oPtr=len(oStack)-1
# using regular expressions for value stack
vStack=re.split('[+ * / -]', exp)
vPtr=len(vStack)-1
i=0
# converting all to float
while i<vPtr+1:
	# syntax checker
	if(vStack[i].isnumeric()):
		vStack[i]=float(vStack[i])
	else:
		exit("invalid syntax")
	i=i+1

# debugging
# print("... processing ...")
# print("values stack: ", vStack)
# print("operator stack: ", oStack)

# solve
print("... processing ...")
i=oPtr
print("values stack: ", vStack)		
print("operator stack: ", oStack)
# solving higher priority operators
while(i>=0):
	if(oStack[i]=='*' or oStack[i]=='/'):
		opn=oStack.pop(i)
		oPtr=oPtr-1
		op1=vStack.pop(i)
		op2=vStack.pop(i)
		vStack.insert(i, solve(op1, op2, opn))
		vPtr=vPtr-1
		print("values stack: ", vStack)		
		print("operator stack: ", oStack)
	i=i-1
# solving low priority operators
i=oPtr
while(i>=0):
	if(oStack[i]=='+' or oStack[i]=='-'):
		opn=oStack.pop(i)
		oPtr=oPtr-1
		op1=vStack.pop(i)
		op2=vStack.pop(i)
		vStack.append(solve(op1, op2, opn))
		vPtr=vPtr-1	
		print("values stack: ", vStack)		
		print("operator stack: ", oStack)
	i=i-1
# debugging

# print("values stack: ", vStack)
# print("operator stack: ", oStack)

# print
print("")
print("The result is: ", vStack[0])
