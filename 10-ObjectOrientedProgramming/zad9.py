"""9.	Write a program in which you create a TV class that describes a TV set. 
The class should contain one boolean field called 'is_on' that specifies whether the TV set is turned on. 
By default, the TV is turned off. Add turn_on() and turn_off() methods in the class to turn the TV on and off, respectively. 
Also add a show_status() method to display whether the TV is on or off. Sample message:
TV is on
Then try using the TV set in the program:
a.	Create TV set
b.	Show TV status
c.	Turn TV on
d.	Show TV status
e.	Turn TV off
f.	Show TV status
"""


class TV:
    def __init__(self):
        self.is_on = False

    
    def turn_on(self):
        self.is_on = True

    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        print(self.is_on)
        
tvset = TV()
for x in range(4):
    if (x%2==0):
        tvset.turn_on()
    else:
        tvset.turn_off()
    tvset.show_status()