"""45.	Create a function that convert two-dimensional (2D) array into 1D. 
Then create a program that displays 1D array for the following 2D arrays.
a.	2 3
    1 5 
b.	5 0 3 7 5
    9 0 9 1 2
c.	2 1
    3 5
    7 4
    2 6
"""

def con(arr2d):
    arr1d = []
    for x in arr2d:
        arr1d += x
    return arr1d



print(con([[2,3],[1,5]]))
print(con([[5,0,3,7,5],[9,0,9,1,2]]))
print(con([[2,1],[3,5],[7,4],[2,6]]))

