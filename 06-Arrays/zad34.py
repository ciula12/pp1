"""34.	Write a program that checks whether the first array 
is a subset of the second one (whether all elements of the first array appear in the second array)."""

def f(arr1,arr2):
    for x in arr1:
        isthere = False
        for y in arr2:
            if x == y:
                isthere = True
                break
        if isthere == False:
            return False
    return True


print(f([1,2,3],[3,2,1]))
print(f([1,2,4,3],[3,2,1]))
print(f([1,2,3],[4,3,2,1]))
print(f([1,2,3,4],[4,3,2,1]))
