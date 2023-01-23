"""33.	The array contains integer numbers from 1 to 999. Write a program that displays elements of the array formatted as below.
-----------------------------------------
|   1|  23|   5| 382|   1|  17|   4| 906|
-----------------------------------------
"""

def f (arr):
    for x in arr:
        print("|",end="")
        if x < 10:
            print("  ", x ,end="")
        elif x < 100:
            print(" ", x ,end="")     
        elif x < 1000:
            print("", x ,end="")   

    print()
    return True





array = []
for x in range(1,1000):
    array.append(x)
print(f(array))