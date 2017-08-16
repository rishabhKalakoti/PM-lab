from basic_defn import *
from variables import *

print(note)

fileObj  = open("hello.c", "r")

# moving braces to different lines
x="\n{\n"
st = x.join(fileObj.read().split("{"))
x="\n}\n"
st = x.join(st.split("}"))
# all statements in differnt lines
x=";\n"
st = x.join(st.split(";"))
# removing tabs
x=""
st = x.join(st.split("\t"))

text = st.split("\n")

# time to get in the game...
print("... Processing ...")

# comments
print("removing comments...")
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

# removing emty lines
for i in range(len(text)):
	text[i] = text[i].strip()	
	if text[i]=="":
		index.append(i)
removeExtra(index, text)

# remove strings
#x='\n'
#st = x.join(text)
#flag=0
#for i in range(len(st)):
#	if(st[i]=='"' and flag==0):
#		flag=1
#	elif(flag==1 and not st[i]=='"'):
#		index.append(i)
#	if(flag==1 and st[i]=='"'):
#		flag=0
#removeExtra(index, st)
#text = st.split("\n")
#print(text)

# brackets order check
print("checking bracket order...")
stack = []
s = ""

s=s.join(text)
#print(s)
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
# preprocessor
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


# the main function
print("the job with the main function...")
mainFlag=0
for i in range(len(text)):
	if "main()" in text[i]:
		mainFlag=1
		index.append(i)
		txt=text[i].split(" ")
		if(not txt[txt.index("main()")-1] in dType):
			mainFlag=-1
		if(not text[i+1]=='{'):
			showError("'{' expected after main()")
		
# the main() function
# checks if main() exists
if(mainFlag==0):
	showError("No main() function. I don't know where to start!")
# checks data type for main() function
elif(mainFlag==-1):
	showError("Incorrect data type assigned to main function")
removeExtra(index, text)

# brackets for a function
# statements
print("statement check...")
for i in range(len(text)):
	if(not text[i] in moreTokens and not text[i].endswith(";")):
		showError("Statement not terminated properly.")

for i in range(len(text)):
	if "{" in text[i] or "}" in text[i]:
		index.append(i)
removeExtra(index, text)

print("checking function call...")
# function call
for i in range(len(text)):
	if "(" in text[i] and ")" in text[i]:
		t=text[i].split('(')[0].lstrip()
		if not t.isalnum():
			showError("Incorrect function call")
print("done.")
# print(text)
print("\nLOOKS GOOD! YOU ARE GOOD TO GO.")
