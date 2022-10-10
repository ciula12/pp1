from tkinter import Y
from pyparsing import null_debug_action


x = 7
y = 34
z = x

print("x= ",x)
print("y= ",y)


x=y
y=z

print("x= ",x)
print("y= ",y)
