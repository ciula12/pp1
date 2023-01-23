"""17.	Create a program that computes the second power of each array element. Sample result:
Array: 8 2 5 1 9
2nd power: 64 4 25 1 81
"""



def f(n):
    for x in n:
        x = x**2
        print(x, end=" ")


f([8,2,5,1,9])