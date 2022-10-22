tablica = []
tablica.append(int(input("First number:")))
tablica.append(int(input("Second number:")))

print(len(tablica))

for x in range(len(tablica)-1):
    print (x)
    if tablica[x]>tablica[x+1]:
        c=tablica[x]
        tablica[x]=tablica[x+1]
        tablica[x+1]=c    




print(f"Numbers in ascending order: {tablica[0]} {tablica[1]}")