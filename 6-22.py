###
# Write a program that prints numbers from 1 to 30. If the number is 
# divisible by 3 then the program prints the word 'THREE'. Next, if the 
# number is divisible by 5 then the program prints the word 'FIVE'. 
# Finally, if the number is divisible by both 3 and 5 then the program 
# prints the word 'BINGO'.
#

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:   # is divisible by 3 & 5
        print("BINGO", end=", ")
    elif num % 3 == 0:
        print("THREE", end=", ")
    elif num % 5 == 0:
        print("FIVE", end=", ")
    else:
        print(num, end=", ")
