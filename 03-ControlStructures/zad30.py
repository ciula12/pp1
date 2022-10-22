'''30.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
Write a program that finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.
Prime numbers: 2 3 5 7 11 …
'''

N= int(input("N: "))
print("Prime numbers: ", end='')

for x in range(2,N+1):
    Prime = True
    for dziel in range(x-1,1,-1):
        if x%dziel == 0:
            Prime = False
    if Prime == True:
        print(x, end=' ')
            