'''8.	Define a function that displays integer numbers from 1 to N. 
Then call the function and display numbers from 1 to 15.'''

def toN(N):
    for x in range(N+1):
        print(x, end=' ')
    print()

toN(15)
toN(25)