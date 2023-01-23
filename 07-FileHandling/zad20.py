"""20.	Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line."""
import random

file = open("py.txt","w")

for x in range(1,51):
    file.write(f"{str(random.randint(100, 999))}\n")

file.close()

file = open("py.txt")

print(file.read())