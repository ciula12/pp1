import json


person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }


person.update({"Surname": "Nowak", "married": False})
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"].append("landline")


print(person)