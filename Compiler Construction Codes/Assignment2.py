
import sys

f = open("inputt.txt",'r')
file = f.readlines()
print(file)
st1= file[0]
st2= file[1]


global count
count=0

def exp():
    global count
    print("exp -> term exp'")
    term()
    exprr()
    
def exprr():
    global count
    if(expr[count] == '+'):
        count = count+1
        print("exp -> exp + term")
        term()
        exprr()
    elif(expr[count] == '-'):
        count = count+1
        print("exp -> exp - term")
        term()
        exprr()
    else:
        print("exp -> null")
 
def term():
    global count
    print("term -> factor term'")
    factor()
    termr()     
        
def termr():
    global count
    if(expr[count] == '*'):
        count = count+1
        print("term -> term * factor")
        factor()
        termr()
    elif(expr[count] == '/'):
        count = count+1
        print("term -> term / factor")
        factor()
        termr()
    else:
        print("term -> null")
    
        
def factor():
    global count
    exponent()
    if(expr[count] == '**'):
        count = count+1
        print("factor -> exponent POW factor")
        factor()
    else:
        print("factor -> exponent")
        exponent()
        
def exponent():
    global count
    if(expr[count] == '-'):
        count = count+1
        print("exponent -> MINUS exponent")
        exponent()
    else:
        print("exponent -> final")
        final()
        
def final():
    global count
    if(expr[count].isnumeric()):
        count = count+1
        print("final -> int")
    elif(expr[count]=='('):
        count = count+1
        print("final -> (exp)")
        exp()
        if(expr[count] != ')'):
            print("\nRejected")
            sys.exit()
        count = count+1
    else:
        print("\nRejected")
        sys.exit()

for i in range(len(file)):
    expr = file[i]       
    l = len(expr)
    expr = expr + '$'
    print(expr)
    
    exp()
    if(l == count):
        print('\nAccepted')
    else:
        print('\nRejected')
