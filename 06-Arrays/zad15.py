"""15.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. 
Create a program that replaces the values of the main diagonal with 1. Use loop statements. 
Display the modified array as below:
1 0 0
0 1 0
0 0 1
"""


def f(n):
    arr = n
    for x in range(3):
        arr[x][x] = 1

    for x in range(len(arr)):
        for y in range(len(arr[0])):
            print(arr[x][y], end=' ')
        print()



f([[0,0,0],[0,0,0],[0,0,0]])