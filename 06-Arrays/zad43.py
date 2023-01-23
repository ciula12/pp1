"""43.	Create a function identity_matrix(n) that returns an identity matrix of size n (https://en.wikipedia.org/wiki/Identity_matrix). 
Then create a function that displays a 2D array in rows and columns. Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8."""

def identity_matrix(n):
    arr1 = [[0 for x in range(n)] for y in range(n)]

    for x in range(len(arr1)):
        arr1[x][x] = 1

    return arr1

def display(arr):
    for x in range(len(arr)):
        print()
        for y in range(len(arr[x])):
            print(arr[x][y], end=" ") 
    print()


display(identity_matrix(3))
display(identity_matrix(5))
display(identity_matrix(8))