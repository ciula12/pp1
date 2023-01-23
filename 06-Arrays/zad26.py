"""26.	Write a program to find the second largest element in an array. Sample result:
Array: [5,1,9,6,1]
Result: 6
"""

def fun(arr):
    arr1 = sorted(arr)
    return arr1[(len(arr1)-2)]

print(fun([5,1,9,6,1]))