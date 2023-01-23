"""24.	Write a program that calculates the number of vowels in the text:
To be, or not to be, that is the question
Use regular expressions and the findall() method.
"""

import re
mess = "To be, or not to be, that is the question"

vowels = re.findall("[aoeiu]",mess)

print(len(vowels))