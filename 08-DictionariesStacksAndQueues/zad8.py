import json


person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person["name"])
print(person["hobby"])
person.update({"Surname": "Nowak", "married": False})


"""
a.	Display contents of the dictionary
b.	Display name
c.	Display hobby
d.	Change surname to Nowak
e.	Change person's marriage status
f.	Add gender: male
g.	Add a new hobby: bicycle
h.	Add work phone to existing phones: 313131444
"""