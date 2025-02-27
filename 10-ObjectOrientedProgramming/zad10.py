"""10.	In the TV class, add the channel_no field indicating the number of the TV channel displayed by the TV set. 
Initially, the TV is set to channel 1. Modify the show_status() method so that it also displays the TV channel number, but only if the TV is turned on:
TV is on, channel 1
Then try using the TV set.
"""

class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    
    def turn_on(self):
        self.is_on = True

    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")


tvset = TV()
for x in range(4):
    if (x%2==0):
        tvset.turn_on()
    else:
        tvset.turn_off()
    tvset.show_status()

