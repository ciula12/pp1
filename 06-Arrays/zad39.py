"""39.	An array contains values: 
[[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
Create a program that modifies the array values to create a multiplication table as below. 
Use loop statements. Display the array.
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25
"""


array = [[1,0,0,0,0],[2,0,0,0,0],[32,0,0,0,0],[4,0,0,0,0],[5,0,0,0,0]]

num = 1
for x in range(len(array)):
    array[x][0] = num
    num += 1

num = 1
for x in range(len(array[0])):
    array[0][x] = num
    num += 1


for x in range(1,len(array)):
    for y in range(1,len(array[x])):
        num = array[x][0]*array[0][y]
        array[x][y]= num





for x in range(len(array)):
    print (array[x])
    