"""41.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last row. Display array values in rows and columns before and after changes."""

arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

print (arr)


for x in range(len(arr)):
    print()
    for y in range(len(arr[x])):
        print(arr[x][y], end=" ") 


print( )

for x in range(len(arr)):
    pom = arr[x][0]
    arr[x][0]=arr[x][(len(arr[x])-1)]
    arr[x][(len(arr[x])-1)] = pom


print( )

for x in range(len(arr)):
    print()
    for y in range(len(arr[x])):
        print(arr[x][y], end=" ") 