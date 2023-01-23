"""14.	An array contains values: [[True,False],[True,True],[False,False]]. 
Create a program that changes values of an array to the opposite. Use a loop statement."""


def f(n):
    arr = n
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == True:
                arr[x][y] = False
            else:
                arr[x][y] = True
    print (arr)


f([[True,False],[True,True],[False,False]])

