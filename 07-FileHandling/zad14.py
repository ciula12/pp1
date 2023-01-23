"""14.	Write a program that calculates the number of lines for any text file. 
The user enters the name of the file from the keyboard. 
Display the result of the calculation (the file name and the number of lines). 
Do not display the contents of the file. Sample result:
File name: countries.txt
Number of lines: 14
"""




def callines(file):
    file = open(file, "r")
    print(f"File name: {file.name}, {len(file.readlines())}")
    file.close()



callines("file12txt")
print()
callines("numbers.txt")

