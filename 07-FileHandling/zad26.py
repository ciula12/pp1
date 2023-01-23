"""26.	Find any text file on the Internet and download it to your computer. 
Then write a program that displays all words with at least six letters from the file. Display each word on a separate line. Use regular expressions."""
import re

file = open("original.txt")

tekst = file.read()
atleast6 = re.findall("\w+", tekst)

print(atleast6)

