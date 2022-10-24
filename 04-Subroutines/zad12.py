'''12.	Define a function sum(N) that for the given natural number N calculates the sum of all natural numbers between 1 and N. 
Apply recursion.
Then create a program that calculates the sum of natural numbers in the range <1,10>.'''


def sum(N):
    
    if N==1:
        return 1
    
    if N<1:
        print("error")

    if N != 0:
        return N + sum(N-1)
    
    
print(sum(10))