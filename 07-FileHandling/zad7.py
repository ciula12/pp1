file = open('countries.txt', 'r')

count = 1

for line in file:
     print(f"{count}. {line}", end="")
     count += 1
