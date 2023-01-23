"""18.	An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and displays the array and the arithmetic mean of array values. 
Use the “for” loop statement."""


def f(n):
    sum= 0
    print(n)
    for x in n:
        sum = sum + x

    print(round((sum/len(n)),2))

f([15, 8, 31, 47, 2, 19])