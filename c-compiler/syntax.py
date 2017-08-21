from basic_defn import *


#___________________________FUNCTIONS START___________________

# *************** function to check function call
def checkFunctionCall(text):
	for i in range(len(text)):
		txt=text[i]
		for j in range(len(txt)):
			k=0
			if("("==txt[j]):
				ptr=j-1
				s=[]
				while(ptr>=k):
					ch=txt[ptr]
					if not (ch in allOp or ch in moreTokens):
						s.insert(0, ch)
					else:
						break
					ptr=ptr-1
				k=j
				x=""
				if not isValidName("".join(s).lstrip()):
					print("".join(s).lstrip())
					showError("Incorrect function call")
# ****************** function done.

# *************** function to remove comments
def removeComments(text, index):
	flag=0
	sFlag=0
	for i in range(len(text)):
		# single line comments
		if text[i].startswith("//"):
			index.append(i)
		# multiline comments	
		if flag==0:
			if text[i].startswith("/*"):
				flag=1
		if flag==1:
			index.append(i)
			if text[i].endswith("*/"):
				flag=0		
	removeExtra(index, text)
# ************** function done.

# ***************** function to remove strings
def removeStrings(text):
	x='\n'
	st = x.join(text)
	text=st.split('"')
	x='"#'
	st = x.join(text)
	text=st.split('"')
	flag=0
	for i in range(len(text)):
		if text[i].startswith("#") and flag==0:
			flag=1
			text.pop(i)
			text.insert(i, string)
		elif text[i].startswith("#") and flag==1:
			flag=0
			text[i]=text[i][1:]
	x=""
	st=x.join(text)
	text=st.split("\n")
	return text
#************* function done.

#___________________________FUNCTIONS END___________________

# print welcome note
print(note)

fileObj  = open("hello.c", "r")
# moving braces to different lines
x="\n{\n"
st = x.join(fileObj.read().split("{"))
fileObj.close()
x="\n}\n"
st = x.join(st.split("}"))
# all statements in differnt lines
x=";\n"
st = x.join(st.split(";"))
# removing tabs
x=""
st = x.join(st.split("\t"))

text = st.split("\n")

print("... Processing ...")

# ************** removing comments
print("removing comments...")
removeComments(text, index)
# **************** comments removed

# removing empty lines and strip
def removeEmptyLines(text, index):
	for i in range(len(text)):
		text[i] = text[i].strip()	
		if text[i]=="":
			index.append(i)
	removeExtra(index, text)
removeEmptyLines(text, index)
# ************************* preprocessor
print("processing the preprocessor...")
for i in range(len(text)):
	if text[i].startswith("#"):
		index.append(i)
		
		preTerms = text[i][1:].split("<")
		#print(preTerms[1])
		if(not len(preTerms) == 2):
			showError("Incorrect preprocessor terms.")
		if(not preTerms[0] in preWords):
			showError("Incorrect preprocessor terms.")
		if(not preTerms[1].endswith(">")):
			showError("Incorrect preprocessor terms.")
		if(not isFileName(preTerms[1].split(">")[0])):
			showError("Incorrect filename specified in the preprocessor")
removeExtra(index, text)
# ************************* preprocessor done

# ***************** remove strings
print("removing strings...")
text=removeStrings(text)
# ***************** strings removed

# ***************** brackets order check
print("checking bracket order...")
stack = []
s = ""
s=s.join(text)
pushChars, popChars = '<({[', '>)}]'
quotes= ["'", '"']
for c in s:
	if c in pushChars :
		stack.append(c)
	elif c in popChars :
		if not len(stack) :
			showError("incorrect brackets or quotes placement")
		else :
			stackTop = stack.pop()
			balancingBracket = pushChars[popChars.index(c)]
			if stackTop != balancingBracket :
				showError("incorrect brackets or quotes placement")
	elif c in quotes:
		stackTop = stack.pop()
		if not stackTop in quotes:
			stack.append(stackTop)
			stack.append(c)
		elif not stackTop==c:
			stack.append(stackTop)
			stack.append(c)
		elif stackTop==c:
			continue
			
if not len(stack)==0 :
	showError("incorrect brackets or quotes placement")
# ***************** brackets order done

# *************************** the main function
print("the job with the main function...")
mainFlag=0
for i in range(len(text)):
	if "main()" in text[i]:
		mainFlag=1
		index.append(i)
		txt=text[i].split(" ")
		if(not txt[txt.index("main()")-1] in returnType):
			mainFlag=-1
		if(not text[i+1]=='{'):
			showError("'{' expected after main()")
		
# checks if main() exists
if(mainFlag==0):
	showError("No main() function. I don't know where to start!")
# checks data type for main() function
elif(mainFlag==-1):
	showError("Incorrect data type assigned to main function")
removeExtra(index, text)
# ************** main() function done

# **************************** if-else functionality
def checkIf(text, i, index):
	if(text[i].startswith("if") and not (text[i][2].isalnum() or text[i][2]=='_')):
		#if()
		if not isLogicExp(text[i][2:].strip()[1:-1]):
			showError("Invalid logical expression in if(...)")
		if not text[i + 1]=="{":
			showError("Expected { after if(...)")
		counter=0
		j=0
		for j in range(i,len(text)):
			if(text[j]=="{"):
				counter=counter+1
			if(text[j]=="}"):
				counter=counter-1
				if(counter==0):
					break
		if text[j+1]=="else":
			index.append(j+1)
		elif text[j+1].startswith("else if"):
			text[j+1]=text[j+1][5:]
			checkIf(text, j, index)
		index.append(i)
for i in range(len(text)):
	checkIf(text, i, index)
removeExtra(index, text)
for i in range(len(text)):
	if text[i]=="else":
		showError("if(...) expected before else")
# ***************************** if statement done *******************

# statements
print("statement check...")
for i in range(len(text)):
	if(not text[i] in moreTokens and not text[i].endswith(";")):
		showError("Statement not terminated properly.")

# remove braces
for i in range(len(text)):
	if "{" in text[i] or "}" in text[i]:
		index.append(i)
removeExtra(index, text)

# check function call
print("checking function call...")
checkFunctionCall(text)
print("done.")


#___________________________________CHECKING DONE_____________________
print("*"*50)
print("#_debugging")
print(text)
print("*"*50)

print("LOOKS GOOD! YOU ARE GOOD TO GO.")
