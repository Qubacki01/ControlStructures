###
# Program that asks for the number of hours of parking,
# then calculates and prints the correct fee.
#

time = int(input('Enter number of hours (full hours only): '))

if time <= 2 and time > 0:
    fee = 5
elif time <= 6 and time > 2:
    fee = 15
elif time > 6:
    fee = 20
else:
    print('! You cannot enter less then 0 !')
    fee = 'INVALID INPUT'

print(f'The fee is: {fee} PLN')


