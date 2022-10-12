
'''
a = 3
b = 4
c = 5
'''



a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

p = (a+b+c)/2

P=(p*(p-a)*(p-b)*(p-c))**(1/2)

print(f"The area of the triangle is: {P}")