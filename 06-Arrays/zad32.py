"""32.	Define a function that returns the elements of the array as a string, 
separated by commas. Using defined functions, display the contents of any array. Sample result:
Array: [5,4,3,2,6,5]
String: 5,4,3,2,6,5
"""

def f(arr):
    result = ""
    for x in arr:
        result = result + str(x) + ","
    return str(result[:(len(result)-1)])

print(f([5,4,3,2,6,5]))