"""12.	In the TV class, add the channels field containing the list of available TV channel names (array). 
Initially, the array should be empty (TV not programmed, no available channels). 
Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and display the list of available channels. 

Sample list of available channels:
Channel list:
1. TVP1
2. TVP2
3. Polsat
4. TVN
5. Filmbox
6. Discovery
Then try using the TV set:
a.	Create a TV set
b.	Show TV status
c.	Turn TV on
d.	Show TV status
e.	Display the list of available channels
f.	Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
g.	Display the list of available channels
h.	Show TV status
i.	Turn TV offs
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
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")

tvset = TV()

tvset.show_status()
tvset.turn_on()
tvset.show_status()
tvset.show_channels()
tvset.add_channel("TVP")
tvset.add_channel("TVP2")
tvset.add_channel("Polsat")
tvset.add_channel("TVN")
tvset.add_channel("Filmbox")
tvset.add_channel("Discovery")
tvset.show_channels()
tvset.show_status()
tvset.turn_off()
tvset.show_status()