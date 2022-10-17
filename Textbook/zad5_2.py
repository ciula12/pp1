x = input("Podaj liczbę: ")
count = 0
suma = 0
najm = 999999999999999999999
najw = -999999999999999999999

if(x == "gotowe"):
    print("Nieprawidłowe wejście")
    quit()

while(x != "gotowe"):
    try:
        liczba = float(x)
        count = count + 1
        suma = suma + liczba
        if(liczba < najm):
            najm = liczba
        if(liczba > najw):
            najw = liczba
    except:
        print("Nieprawidłowe wejście")

    x = input("Podaj liczbę: ")
    

print(f"Suma: {suma}")
print(f"Ilość podanych liczb: {count}")
print(f"Średnia: {suma/count}")    
print(f"Najmniejsza liczba: {najm}")
print(f"Największa liczba: {najw}")