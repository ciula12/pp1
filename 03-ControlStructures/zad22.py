'''
22.	Write a program that displays numbers from 1 to 30. If the number is divisible by 3 then the program displays the word 'THREE'. Next, if the number is divisible 
by 5 then the program displays the word 'FIVE'. Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. Sample result:
1 2 THREE 4 FIVE THREE 7 ...
'''

for x in range(1,31):
    if (x%3)==0 and (x%5)==0:
        print(f"{x} BINGO")
    else:
        if (x%3)==0:
            print(f"{x} THREE")
        elif (x%5)==0:
            print(f"{x} FIVE")
        else:
            print(x)        
    