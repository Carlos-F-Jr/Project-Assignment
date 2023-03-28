import re

file = open("input_scode.txt")

operators = {'=' : 'operator', '<' : 'operator' }
operators_key = operators.keys()

keyword = ['while']

seperator = { '(' : 'seperator', ')' : 'seperator', ';' : 'seperator' }
seperater_key = seperator.keys()

dataFlag = False

a=file.read()

program = a.split("\n")
print("token ---------- lexems\n")
for line in program:
    tokens=line.split(' ')
    for token in tokens:
        if token in operators_key:
            print(token ,"----------", operators[token])
        elif token in keyword:
            print(token ,"---------- keyword")
        elif token in seperater_key:
            print (token ,"----------", seperator[token])
        else:
            try:
                variable = int(token)
                variable = float(token)
            except ValueError:
                variable = None
            if variable:
                print (token ,"---------- real")
            elif token == ' ':
                pass
            else:
                print (token ,"---------- identifier")
 
    dataFlag=False