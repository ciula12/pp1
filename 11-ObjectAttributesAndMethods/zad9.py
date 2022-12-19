'''9.	In the Arrays class, add three static methods that:
a.	create an array with a given number of elements with the same values. Use list.append():

method_name(number_of_array_elements, value_of_array_elements)

b.	create an array with a given number of elements and the random value of these elements in the range of <m, n>:
 
method_name(number_of_array_elements, value_from, value_to)

c.	determines the number of array elements whose values are in the given range <m, n>:

method_name(array, value_from, value_to)

Then, write a program that creates a 10-element array with element values equal to 4 and a 20-element array of random integers in the range of <-7,8>. 
Display the contents of arrays and calculate how many values between <-1,1> are contained in a 20-element array.
'''
import random


class Arrays():

    @staticmethod
    def append(number_of_array_elements, value_of_array_elements):
        a=[]
        for x in range(number_of_array_elements):
            a.append(value_of_array_elements)
        return(a)

    @staticmethod
    def method2(number_of_array_elements, value_from, value_to):
        b=[]
        for x in range(number_of_array_elements):
            b.append(random.randint(value_from, value_to))
        return(b)

       
    
    @staticmethod
    def method3(array, value_from, value_to):
        c = 0
        for x in array:
            if x >= value_from and x<= value_to:
                c += 1
        return(c)

        

print(Arrays.append(10, 4))
gggg = Arrays.method2(20, -7, 8)
print (gggg)
print(Arrays.method3(gggg, -1, 1))