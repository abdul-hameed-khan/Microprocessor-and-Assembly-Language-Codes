
import re

file = open("code_with_comments.py","r") #reading file

r = file.read()
print(type(r))

x = re.search("[//][A-Za-z0-9]*", r)    
y= re.search("(\")(\")(\")[A-Za-z0-9]*", r)

if x or y:
    print("there is comment in the file")
else:
    print("there is not any comment in the file")




