"""(p2.py) Create a function f(human_age) that returns a dog's age in dogs years. 
For the first two years, each dog year is equal to 10 human years. After that, each dog year is equal to 4 human years. Example:
f(15) => 72
f(2) = > 20
"""

def f(human_age):
    dog_age = 0
    if human_age == 1 or human_age==2 or human_age == 0:
        return(human_age*10)
    human_age -= 2
    dog_age = 20
    return (dog_age+(human_age*4))




for x in range(16):
    print(f"{x} human years in dog years is: {f(x)}")