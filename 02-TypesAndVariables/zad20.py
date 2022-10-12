import random

S = 0

for x in range(3):
    d = random.randint(1, 6)
    print(f"{x+1}. dice: {d}")
    S = S + d

print(f"Sum = {S}") 