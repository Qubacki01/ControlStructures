###
# Write a program that converts a decimal number into a binary number.
#

dec_num = int(input('Enter decimal number: '))

remainders = []                                 # List to store remainders

while dec_num > 0:
    remainder = dec_num%2                       # Loop to divide until done
    remainders.append(str(remainder))           # Add remainder to end of list 
    dec_num = dec_num//2

bin_num = ''.join(remainders[::-1])       # Reverse the list to get binary

print(f'{dec_num}(10) = {bin_num}(2)')