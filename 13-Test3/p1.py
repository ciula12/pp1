"""(p1.py) Define a function f(n) that represents any integer n using sticks. 
The function returns a string containing as many sticks as indicated by the number. 
For efficient calculations, the sticks are grouped in groups of five and separated by a minus sign. Example:
f(-4)  ""
f(0)  ""
f(5)  "/////"
f(7)  "/////-//"
f(10)  "/////-/////"
f(11)  "/////-/////-/"
"""

def f(n):
    c = ""
    if n<1:
        return ""
    else:
        if n<6:
            for x in range(n):
                c = c + "/"
            return c
        else:
            for x in range(1,n+1):
                c = c + "/"
                if (x%5==0) & (x!=0):
                    c = c + "-"
            return c
            

print(f(-4))
print(f(0))
print(f(5))
print(f(7))
print(f(10))
print(f(11)) 