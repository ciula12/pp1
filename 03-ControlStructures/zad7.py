x = input("Number: ")


try:
    x = int(x)
    if((x%2)==0):
        print("even")
    else:
        print("not even")
except:
    print("Error")
