"""(p4.py) The computer system registers all entries into the car park ("in") 
and exits from the car park ("out"). Define the function f(d), 
which for the given data will return an array containing the registration numbers
of the vehicles that remain in the car park, in alphabetical order. Example:
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
f(cars)  ["BA111","GX444","KR234"]
"""

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

def f(d):
    cars_in=[]
    for x in range(len(d)):
        car, status = d[x]
        if (status=="in"):
            cars_in.append(car)
        else:
            cars_in.remove(car)
    return sorted(cars_in)




print(f(cars))