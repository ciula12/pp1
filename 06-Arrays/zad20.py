"""20.	An array contains integer numbers: 12, 6, 4, 9, 10. 
Create a program that displays the array values graphically as below. 
Define a function star(n) that returns the given number of asterisks as a string. 
Use a defined function in the program.
12: ************
6: ******
4: ****
9: *********
10: **********
"""

def f(n):
    for x in n:
        print(f"{x}:",int(x)*"*")


f([12, 6, 4, 9, 10])