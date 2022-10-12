'''
Write a program that enables the user to face the computer. The computer throws a dice. 
The user then tries to guess the number from a dice by entering a number from 1 to 6 from the keyboard. 
If the user has guessed the number from the dice, the computer displays True
'''
import random

d = random.randint(1, 6)

g = int(input("Guess dice number: "))

while g > 6 or g < 1: 
    print("not possible choice")
    g = int(input("Guess dice number again (from 1 to 6): "))

print (True) if g == d else print(False)