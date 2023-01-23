"""30.	Create a function minmax(array) that, for the given array of integers, 
returns a two-element array containing the smallest and largest values in the given array. Sample result:
Array:  [4,2,8,4,7,9,5]
Result: [2,9]
"""

def minmax(arr):
    result = []
    arr1 = sorted(arr)
    result.append(arr1[0])
    result.append(arr1[(len(arr1)-1)])
    return result


print(minmax([4,2,8,4,7,9,5]))
print(minmax([0,4,2,8,4,7,9,5]))
print(minmax([4,8,4,7,13,9,5]))