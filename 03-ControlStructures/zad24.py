max = int(input("Number: "))

for x in range(1,(max+1)):
    for c in range(0,x):
        print("*", end='')
    print()    

for x in range((max+1),1,-1):
    for c in range(0,x):
        print("*", end='')
    print()    

    