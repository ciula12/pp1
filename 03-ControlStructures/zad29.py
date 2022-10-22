'''29.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard.
Entering 0 ends entering numbers. Sample result:
Enter number: 15
Enter number: 8
Enter number: 10
Enter number: 0
RESULT: Quantity=3, Sum=33, Mean=11
'''

x = float(input("Enter number: "))
Quantity = 0
Sum = 0

while x != 0:
    Quantity += 1
    Sum = Sum + x
    x = float(input("Enter number: "))


print(f"Result: ", end='')
print(f"Quantity = {Quantity}, ", end='')
print(f"Sum = {Sum}, ", end='')
print(f"Mean =  {Sum/Quantity}")





