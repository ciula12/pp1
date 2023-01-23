"""42.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last column. 
Display array values in rows and columns before and after changes."""

def display(arr):
    for x in range(len(arr)):
        print()
        for y in range(len(arr[x])):
            print(arr[x][y], end=" ") 
    print()

arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
display(arr)

pom = arr[0]
arr[0]=arr[(len(arr)-1)]
arr[(len(arr)-1)] = pom

display(arr)

