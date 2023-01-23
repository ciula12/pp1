"""25.	Write a program that computes the number of words in the following text. Use regular expressions.
To be, or not to be, that is the question
"""
import re
mess = "To be, or not to be, that is the question"

words = re.findall("\w+", mess)
print (words)