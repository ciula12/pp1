x = input("First number: ")
y = input("Second number: ")

try:
    x = int(x)
    y = int(y)

    if(x > 0 or y > 0):
        print("At least one of the numbers is positive")
    else:
        print("None of the numbers is positive")
    

except:
    print("At least one of the numbers contain error")
