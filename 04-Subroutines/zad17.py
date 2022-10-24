'''17.	Create a program that calculates how many times the given letter appears in any text. 
Then create a program and check how many times the letter e’ appears in the text below. 
Define a function for making calculations.
You never get a second chance to make a first impression
'''


def eeeee(letter, text):
    count = 0

    for x in range(len(text)):
        if letter == text[x]:
            count +=1
    return count



print(eeeee(str("e"), str("You never get a second chance to make a first impression")))
