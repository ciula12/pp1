"""19.	Create a program that writes to a text file integer numbers in the range of <1,50>, every number in a separate line."""


file = open("py.txt","w")

for x in range(1,51):
    file.write(f"{str(x)}\n")

file.close()

file = open("py.txt")

print(file.read())