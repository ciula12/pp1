"""
8.	Add a fullname field to the University class that contains the full name of the university, and the print_fullname() and set_fullname() 
methods to display and change the full name of the university. Then create an object and:
a.	display short university name
b.	display full university name
c.	change university name
d.	change full university name
e.	display short university name
f.	display full university name

"""

class University():

    def __init__(self):
        self.name = 'CUE'  
        self.fullname = ""

    def print_name(self):
        print(self.name)

    def change_name(self,name):
        self.name = name
    
    def change_fullname(self, fullname):
        self.fullname = fullname

    def print_fullname(self):
        print(self.fullname)

uni = University()

uni.print_name()
uni.print_fullname()
uni.change_name("MIT")
uni.change_fullname("Massachusetts Institute of Technology")
uni.print_name()
uni.print_fullname()