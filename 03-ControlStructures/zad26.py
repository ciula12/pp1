'''
26.	The payment card is secured with a four-digit PIN code (0805). Write a program that checks if the PIN code entered in the payment terminal is correct. 
The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. Sample result:
Enter the PIN code: 2398
Incorrect...
Enter the PIN code: 0912
Incorrect...
Enter the PIN code: 7860
Incorrect...
Sorry, your payment card has been blocked.
'''

PIN = "0805"
enternumber = 1

userent = input("Enter the PIN code: ")

while(PIN != userent):
    print("Incorrect...")
    enternumber = enternumber + 1
    if enternumber>3:
        print("Sorry, your payment card has been blocked.")
        quit()
    userent = input("Enter the PIN code: ")


