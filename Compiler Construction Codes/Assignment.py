
import sys

exp = input("Enter the expression: ")  
global count
count=0

def E():
    print("E -> TE'")
    T()
    EP()
    
    
def EP():
    global count
    if(exp[count] == '+'):
        count = count+1
        print("E' -> +TE'")
        T()
        EP()
    elif(exp[count] == '-'):
        count = count+1
        print("E' -> -TE'")
        T()
        EP()
    else:
        print("E' -> null")
    
    
def T():
    global count
    print("T -> FT'")
    F()
    TP()
    
def TP():
    global count
    if(exp[count] == '*'):
        count = count+1
        print("T' -> *FT'")
        F()
        TP()
    elif(exp[count] == '/'):
        count = count+1
        print("T' -> /FT'")
        F()
        TP()
    else:
        print("T' -> null")
        return None
    
        
def F():
    global count
    if(exp[count].isalpha()):
        count = count+1
        print("F -> id")
    elif(exp[count].isnumeric()):
        count = count+1
        print("F -> num")
    elif(exp[count]=='('):
        count = count+1
        print("F -> (E)")
        E()
        if(exp[count] != ')'):
            print("\nRejected")
            sys.exit()
        count = count+1
    else:
        print("\nRejected")
        sys.exit()
            
        
        
# def isalpha(c):
#     if(re.match("[A-Za-z]*", c)):
#         return True
#     else:    
#         return False
# def isdigit(cn):
#     if(re.match("[0-9]",cn)):
#     # if(c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c='7' or c=='8' or c=='9'):
#         return True
#     else:
#         return False

  

l = len(exp)
exp = exp + '$'
print(exp)

E()
if(l == count):
    print('\nAccepted')
else:
    print('\nRejected')
        
        
# """
# Created on Mon Nov 29 08:36:33 2021

# @author: Abdul Hameed Khan
# """
# import re
# global count
# count=0

# def E():
#     print("E -> TE'")
#     T()
#     EP(count)
    
    
# def EP(count):
#     if(exp[count] == '+'):
#         count = count+1
#         print("E' -> +TE'")
#         T()
#         EP(count)
#     elif(exp[count] == '-'):
#         count = count+1
#         print("E' -> -TE'")
#         T()
#         EP(count)
#     else:
#         print("E' -> null")
    
    
# def T():
#     print("T -> FT'")
#     F(count)
#     TP(count)
    
# def TP(count):
#     if(exp[count] == '*'):
#         count = count+1
#         print("T' -> *FT'")
#         F(count)
#         TP(count)
#     elif(exp[count] == '/'):
#         count = count+1
#         print("T' -> /FT'")
#         F(count)
#         TP(count)
#     else:
#         print("T' -> null")
        
# def F(count):
#     if(isalpha(exp[count])):
#         count = count+1
#         print("F -> id")
#     elif(isdigit(exp[count])):
#         count = count+1
#         print("F -> num")
#     elif(exp[count]=='('):
#         count = count+1
#         print("F -> (E)")
#         E()
#         if(exp[count] != ')'):
#             print("\nRejected")
#         count = count+1
#     else:
#         print("\nRejected")
            
        
        
# def isalpha(c):
#     if(re.match("[A-Za-z]*", c)):
#         return True
#     else:    
#         return False
# def isdigit(cn):
#     if(re.match("[0-9]",cn)):
#     # if(c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c='7' or c=='8' or c=='9'):
#         return True
#     else:
#         return False


# exp = input("Enter the expression: ")    



# l = len(exp)
# E()
# if(l == count):
#     print('\nAccepted')
# else:
#     print('\nRejected')
        
        