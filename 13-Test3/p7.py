"""(p7.py) A class C contains the following static/class methods:
m1(n) - returns a number based on n, with the odd digits removed
m2(n) - returns true when each subsequent digit in a number n is equal to or greater than the previous digit or false otherwise
m3() - returns a string, with the digits missing from the number n, in ascending order
Example:
C.m1(4231564)  4264
C.m1(79381)  8
C.m2(125579)  True
C.m2(4557879)  False
C.m3(23557)  "014689"
C.m3(12340)  "56789"
"""

class C:   
    
    def m1(n):
        text = n
        result = ""
        for x in str(text):
            if int(x)%2==0:
                result = result + str(x)
        print(result)
        return(result)

    def m2(n):
        text = str(n)
        for x in range(len(text)-1):
            if int(text[x])>int(text[x+1]):
                print(False)
                return(False)
        print(True)
        return(True)

    def m3(n):
        text = str(n)
        result=""
        for x in range(10):
            isnum= False
            for h in range(len(text)):
                if (x==int(text[h])):
                    isnum = True
            if isnum == False:
                result = result + str(x)
        print(result)
        return(result)
            



C.m1(4231564) 
C.m1(79381)
C.m2(125579)
C.m2(4557879) 
C.m3(23557) 
C.m3(12340)