"""(p6.py) Create a function f(age, course, average) that, 
for the data.json file, returns the number of students who have at least the given number of years 
and have at least the given grade average in the given course. 
Example:
f(21, "statistics", 4) => compare results with other students

"""
import json

def f(age, course, average):
    w = []
    file = open("data.json")
    jfile = json.load(file)
    for i in jfile:
        if i["age"]>age:
            print(i["age"])
            print(i["studies"]["courses": "name"])
    

    


f(21, "statistics", 4)