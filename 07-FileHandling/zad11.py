"""11.	An array film_titles contains any five film titles. Write a program that writes the film titles to a text file, each title on a separate line."""

arr = ["film1", "film2", "film3", "film4", "film5"]

file = open("zad10txt","w")

for x in arr:
    file.write(f"{x}\n")

file = open("zad10txt","r")
print(file.read())