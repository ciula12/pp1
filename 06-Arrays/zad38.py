"""38.	A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. 
Create a program and the function. 
Then create a two-dimensional array with dimensions of 3 by 5. Display the created array."""

def create_2d_arr(x,y):
    array = [],[]
    for i in range(x):
        array[0].append(0)

    for j in range(y):
        array[1].append(0)
    
    return array


print(create_2d_arr(3, 5))

