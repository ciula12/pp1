"""31.	Write a program to separate even and odd numbers of a given array of integers. 
Put all even numbers first, and then odd numbers."""

def f(arr):
    even = []
    odd = []
    result = []
    for x in arr:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    
    result = even + odd
    return result


print(f([4,1,3,8,4,7,13,2,9,5]))