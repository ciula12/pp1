"""(p3.py) Create a function f(array2D) that returns a one-dimensional array containing the sums of the columns in a given two_dimensional array. Example:
f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) => [14,19,6,16]
"""


def f(array2D):
    arr1 = []
    for y in range(len(array2D[0])):
        counter = 0
        for x in range(len(array2D)):
            counter += array2D[x][y]
        arr1.append(counter)
    return arr1

    


print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9]]))