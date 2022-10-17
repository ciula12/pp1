x = input('Podaj wartość pomiędzy 0.0 a 1.0: ')

try:
    wart = float(x)
    while(wart > 1.0 or wart < 0.0):
        x = input('Podaj wartość numeryczną pomiędzy 0.0 a 1.0: ') 
        wart = float(x)
    if(wart < 0.5):
        ocena = 2.0
    elif(wart < 0.6):
        ocena = 3.0
    elif(wart < 0.7):
        ocena = 3.5
    elif(wart < 0.8):
        ocena = 4.0
    elif(wart < 0.9):
        ocena = 4.5
    else:
        ocena = 5.0
    
    print(f"Ocena: {ocena}")

except:
    print ("Błąd, podaj wartość numeryczną")


