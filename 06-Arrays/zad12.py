def f(n):
    arr = n
    print(len(arr))
    print(len(arr[0]))
    print(arr[0][1])
    print(arr[1][2])
    for x in range(len(arr[1])):
        print(arr[1][x], end=" ")
        
    print()        
    print("____________")
    
    for x in range(len(arr)):
        for y in range(len(arr[1])):
            print(arr[x][y], end=" ")
        print()
   
    print("____________")
    
    for x in range(len(arr)):
        print(arr[x][2])


f([[2,5,4],[9,0,3]])