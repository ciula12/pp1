"""12.	Create a program that allows you to add a name of next 
product you want to buy at the end of the text file shopping.txt. 
Enter the product name from the keyboard. Tip: open the file in appending mode"""




def nextproduct(product):
    file = open("file12txt","a")

    file.write(f"{product}\n")
    file.close
    




nextproduct("egg")
nextproduct("water")


file = open("file12txt","r")
print(file.read())