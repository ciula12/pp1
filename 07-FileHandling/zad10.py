"""10.	Create a program that saves, 
in separate lines, your name and surname, university name and field of study in a text file.  
Tip: open a file in writing mode and then use the write() method."""

file = open("filezad10","w")

file.write("Wawrzyniec\nCiuła\nUEK\nInformatyka")

file = open("filezad10", "r")
print(file.read())
