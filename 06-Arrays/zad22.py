"""22.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
Create a program that displays the numbers from the first array that do not appear in the second array."""

def function(arr1, arr2):
    for i in arr2:
        for j in arr1:
            if i==j:
                arr1.remove(j)
    return arr1


print(function([4,36,12,28,9,44,5], [5,1,36]))