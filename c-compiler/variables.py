# lexical replacements
string = "$_STRING"

logicOp_lex = "$_LOGIC_OP"
logicOp_NOT = "$_LOGIC_NOT"
compOp_lex = "$_COMP_OP"
arithOp_lex = "$_ARITH_OP"

# welcome note
note="*"*50 + "\nNOTE:-\tThis syntax checker is not perfect.\n\
\tUse only double quotes not single quotes.\n\
" + "*"*50

# all operators
allOp = ["&&", "||", "!", "==", "!=", "<=", ">=", ">", "<", "+", "-", "*", "/", "%", "=", ","]
# logical operators
logicOp = ["&&", "||", "!"]
# comparision operators
comparisionOp = ["==", "!=", "<=", ">=", ">", "<"]
# arithmetic operators
arithmeticOp = ["+", "-", "*", "/", "%"]
# data types
dataType = ["int", "char", "float", "double"]
# function return types
returnType = ["int", "char", "float", "double", "void"]
# preprocesor terms
preWords = ["include", "define"]
moreTokens = ["(", ")", "{", "}"]
index = []
variables = []

# for extra error info
errInfo=""
