"""21.	Create a program that saves to a text file, numbers in the range of <1,10> with their second and third power. Sample result:
1,1,1
2,4,8
3,9,27
4,16,64
…
"""

file = open("py.txt","w")

for x in range(1,11):
    file.write(f"{x} {x**2} {x**3}\n")

file.close()

file = open("py.txt")
print(file.read())