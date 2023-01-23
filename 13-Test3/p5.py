"""(p5.py) The object created from a class C contains an array of integers, 
passed in when the object is created. 
Define a text representation of an object that returns an expression that sums up all the numbers in an array, 
in the order as in the array. 
Example:
C([5,12])  "5+12=17"
C([6,0,15])  "6+0+15=21"
"""

class C:
    def __init__(self,arr):
        self.arr = arr
        sum = 0
        wynik = ""
        for x in range(len(arr)):
            sum = sum + arr[x]
        for x in range(len(arr)):
            wynik = str(wynik) + "+" + str(arr[x])
        wynik = wynik[1:len(wynik)]
        wynik = wynik + "=" + str(sum)
        print(wynik)
        
    
ob = C([5,12])
ob = C([6,0,15])


