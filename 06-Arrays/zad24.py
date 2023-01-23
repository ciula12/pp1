"""24.	Create a program that displays all unique elements in an array. Sample result:
Array: 2 3 2 5 8 1 9 8
Unique elements: 3 5 1 9
"""

def fun(arr):
    result = []
    for x in range(len(arr)):
        pom = 0
        for i in range(len(arr)):
            if x!=i:
                if arr[x]==arr[i]:
                    pom = 1
        if pom == 0:
            result.append(arr[x])

    return result
                



print(fun([2, 3, 2, 5, 8, 1, 9, 8]))