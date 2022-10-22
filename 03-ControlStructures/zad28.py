'''
28.	Write a program that displays the first fifty words of the Fibonacci sequence. The sequence is defined as follows: 
the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result below. 
https://en.wikipedia.org/wiki/Fibonacci_number
0 1 1 2 3 5 8 13 21 34 ...
'''


max= 50

Fibonacci = []
Fibonacci.append(0)
Fibonacci.append(1)

print(Fibonacci)

for x in range (2,51):
    Fibonacci.append(((Fibonacci[x-2])+(Fibonacci[x-1])))

print(Fibonacci)