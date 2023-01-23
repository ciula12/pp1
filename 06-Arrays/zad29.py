"""29.	Write a program that, for the given array of real numbers, 
displays the number of elements that are greater than the given value entered from the keyboard."""


def f(num, arr):
    result = 0
    for x in arr:
        if x>num:
            result +=1

    return result




print(f(21,[15,64,81,21,11,0,2,3,13,4,67]))
print(f(2,[15,64,81,21,11,0,2,3,13,4,67]))
print(f(187,[15,64,81,21,11,0,2,3,13,4,67]))
print(f(53,[15,64,81,21,11,0,2,3,13,4,67]))
print(f(10,[15,64,81,21,11,0,2,3,13,4,67]))