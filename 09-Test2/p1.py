"""(p1.py) The playing cards have the following values: 
Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. 
The other cards have the value indicated by the card number. 
Create a function f(player1,player2) that returns true if the first player has cards of higher value, and false otherwise. Example:
f("AJ972","AQT72") => False
f("9532","K8") => True
f("987","AT4") => False
"""


def f(player1,player2):
    p1=0
    p2=0
    for x in range(len(player1)):
        if player1[x].isnumeric():
            p1+=int(player1[x])
        else:
            p1+=10

    for x in range(len(player2)):
        if player2[x].isnumeric():
            p2+=int(player2[x])
        else:
            p2+=10

    print( p1>p2)
    return p1>p2
    
            

f("AJ972","AQT72")
f("9532","K8")
f("987","AT4")