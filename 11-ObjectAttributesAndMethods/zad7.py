'''7.	The student has a name, surname, ID (album number) and a field of study. All students study at the same university (UEK Kraków). 
Create a class describing a student. 
Student ID should be assigned automatically as a sequential natural number starting from 100000. 
For this purpose, create a class variable to store the last student’s ID number. 
When creating a new student (object), increase the value of this variable by one and then use it as the identifier of the created student. 
Then write a program that creates 3 different students and displays their personal data in the format as below. Use the __str__ method.
Anna MAJ (100001), Applied Informatics, UEK Kraków
'''


class Student():
    ID = 100000
    uni = "UEK Krakow"
    def __init__(self, name, surname, fieldofstudy):
        self.name = name
        self.surname = surname
        self.fieldofstudy = fieldofstudy
        Student.ID += 1
        

    def __str__(self):
        return f"{self.name} {str.upper(self.surname)} ({Student.ID}), {self.fieldofstudy}, {Student.uni}"

    


student1 = Student("Anna", 'Maj', "Applied Informatics")
print(student1)
student2 = Student("Kasia", 'Niemaj', "Economics")
print(student2)
student3 = Student("Kacper", 'Kwiecień', "Applied Informatics")
print(student3)