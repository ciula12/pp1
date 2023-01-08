"""11.	Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. Then try using the TV set.
a.	Create a TV set
b.	Show TV status
c.	Turn TV on
d.	Show TV status
e.	Change TV channel to 5
f.	Show TV status
g.	Turn TV off
h.	Show TV status 
"""



class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
    

    
tvset = TV()

tvset.show_status()
tvset.turn_on()
tvset.show_status()
tvset.set_channel(5)
tvset.show_status()
tvset.turn_off()
tvset.show_status()