"""18.	Using any text editor, create the following two text files:
MeatAndFish.txt
Skinless white meat
Tuna fish
Luncheon meat
Lean cuts of red meat
GrainsAndBread.txt
Bread
Rice
All purpose flour
Breakfast cereal
Pasta 
Then write a program that creates a shoppinglist.txt file, in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.
"""

file = open("shoppinglist.txt", "w")
file1 = open("MeatAndFish.txt")
file2 = open("GrainsAndBread.txt")


pom1 = file1.read()
pom2 = file2.read()

file.write(pom1)
file.write(pom2)
file.close()

file = open("shoppinglist.txt")
print(f"Lista zakupów:\n{file.read()}")

