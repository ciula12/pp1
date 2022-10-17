from telnetlib import SGA


liczbag = 20 
sg = input("Stawka godzinowa: ")
wyn = 0

try:
    stawkag = float(sg)
    if(liczbag > 40):
        wyn = 40 * stawkag
        stawkag = stawkag * 1.5
        liczbag = liczbag - 40
        wyn = wyn + liczbag * stawkag
    else:
        wyn = stawkag * liczbag
    
    print(wyn)
except:
    print("Błąd, podaj wartość numeryczną")







