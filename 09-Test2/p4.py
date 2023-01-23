"""(p4.py) Create a function f(dictionary,x,y) that returns the sum of numbers in the range <x,y> contained in the dictionary. 
Example:
f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) => 16
f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) => compare results with other students
"""


def f(dictionary,x,y):
    result = 0
    for i in dictionary.keys():
        
        for j in dictionary[i]:
            if j==x:
                result+=x
            if j==y:
                result+=y
    return result
            

    



    return True

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))