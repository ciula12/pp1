am = input("Enter the amount in PLN: ")


while True:
    try:
        am = int(am)
        break
    except:
        am = input("Enter integer the amount in PLN: ")
    
print(f"The amount of PLN {am} in coins:")

fives = am//5
am = am%5

twos = am//2
am = am%2

ones = am

print(f"5 zł - {fives}")
print(f"2 zł - {twos}")
print(f"1 zł - {ones}")