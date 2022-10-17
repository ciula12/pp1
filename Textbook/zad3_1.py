liczbag = 45
stawkag = 10
wyn = 0

if(liczbag > 40):
    wyn = 40 * stawkag
    stawkag = stawkag * 1.5
    liczbag = liczbag - 40
    wyn = wyn + liczbag * stawkag


print(wyn)
