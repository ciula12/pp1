"""19.	An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and displays the array and the arithmetic mean of array values. 
Use the “while” loop statement."""

def f(n):
    print(n)
    sum= 0 
    length = len(n)
    while n:
        sum = sum + n.pop()
    print(round((sum/length),2))

        




f([15, 8, 31, 47, 2, 19])