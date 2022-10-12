'''
23% VAT was paid from the amount of PLN 15.84. Calculate and display VAT. Apply formatting with decimal places. Sample result:
Amount  : 15.84 zł
VAT 23% :  3.64 zł
'''



VAT = 0.23
A = float(input("Amount: "))


print(f"Amount: {A} zł")
print(f"VAT 23%: {round(A * VAT ,2)} zł")


