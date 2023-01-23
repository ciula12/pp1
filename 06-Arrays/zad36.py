"""36.	A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that displays array values in rows and columns."""

array = [[1,2,3,4],[5,6]]


print(array)
print(len(array))
print(len(array[0]))

print("____________")
for x in range(len(array)):
    print()
    for y in range(len(array[x])):
        print(array[x][y], end=" ")