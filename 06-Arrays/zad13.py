"""13.	An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]].
Create a program that calculates the sum of all even numbers. """

def f(n):
    sum = 0
    arr = n
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if int(arr[x][y])%2==0:
                sum += int(arr[x][y])
    print(sum)




f([[3,9,2],[2,4,5],[7,1,6],[0,4,8]])