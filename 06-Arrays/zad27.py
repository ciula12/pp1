"""27.	Write a program that displays the difference between the largest and smallest values in an array of integers. Sample result:
Array: [5,1,9,6,1]
Result: 8
"""


def fun(arr):
    result = sorted(arr)
    return (result[(len(arr)-1)]-result[0])

print(fun([5,1,2,19,6,1]))