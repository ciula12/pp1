import random

x = random.randint(-100,100)
y = random.randint(-100,100)

while x == 0 or y == 0:
    x = random.randint(-100,100)
    y = random.randint(-100,100)

if x>0:
    if y>0:
        quadrant = "first"
    else:
        quadrant = "fourth"
else:
    if y>0:
        quadrant = "second"
    else:
        quadrant = "third"

print(f"Point P({x}|{y}) is in the {quadrant} quadrant of the coordinate system")
