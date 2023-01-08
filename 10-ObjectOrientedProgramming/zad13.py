"""13.	In the TV class, make changes to the show_status() method so that it displays not only the selected channel number but also its name. 
When the selected channel number exceeds the list of available channels, the channel name is not displayed.
TV is on, channel 4 (TVN)
Then try using the TV. Set at least 7 channels (seven TV stations), change the channel numbers and display TV status every time.
"""

class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []

    def add_channel(self,channel_name):
        self.channels_list.append(channel_name)

    def show_channels(self):
        print(self.channels_list)
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}", end=" ")
            if len(self.channels_list)>=self.channel_no:
                print(f"({self.channels_list[self.channel_no-1]})")
            else:
                print()

        else:
            print("TV is off")

tvset = TV()

tvset.show_status()
tvset.turn_on()
tvset.add_channel("TVP")
tvset.add_channel("TVP2")
tvset.add_channel("Polsat")
tvset.add_channel("TVN")
tvset.add_channel("Filmbox")
tvset.add_channel("Discovery")
tvset.show_status()
for x in range(2,8):
    tvset.set_channel(x)
    tvset.show_status()
tvset.turn_off()
tvset.show_status()