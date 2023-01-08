file = open("numbers.txt", "r")


sum = 0
numb = ""
for line in file:
    numb = numb + str(int(line)) + " + " 
    sum = sum + int(line)
    print(numb[:(len(numb))-2], end="")
    print("=", sum)

