"""(p5.py) Create a function f(first_letter,last_letter) that, for the data.txt file, 
returns the number of words that start with the first_letter and end with the last_letter. 
Example:
f("w", "d") => compare results with other students 
"""

import re
print("______________________________________")

file = open("data.txt", encoding="utf8")
text = file.read()

result = re.findall(r"\bw\w+d\b",text)
print(len(result))






