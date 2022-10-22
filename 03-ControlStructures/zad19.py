hyears = input("Enter the dog's age in human years: ")
dyears = 0



while True:
    try:
        hyears = int(hyears)
        break
    except:
        hyears = input("Enter the dog's age in integer human years: ")

if hyears <= 0:
    print("Invalid age of dog")
    quit()

if hyears>=2:
    hyears = hyears - 2
    dyears = 10.5
else:
    dyears = 5.25

dyears = dyears + hyears*4

print(f"The dog's age in dog’s years is {dyears} years.")




