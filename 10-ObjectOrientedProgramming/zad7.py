class University():

    def __init__(self):
        self.name = 'CUE'    

    def print_name(self):  
        print(self.name)

    def set_name(self, name):
        self.name = name



ob = University()
ob.set_name("MIT")
print(ob.name)