x = input("Podaj liczbę: ")
count = 0
suma = 0

if(x == "gotowe"):
    print("Nieprawidłowe wejście")
    quit()

while(x != "gotowe"):
    try:
        liczba = float(x)
        count = count + 1
        suma = suma + liczba
    except:
        print("Nieprawidłowe wejście")

    x = input("Podaj liczbę: ")
    

print(f"Suma: {suma}")
print(f"Ilość podanych liczb: {count}")
print(f"Średnia: {suma/count}")    