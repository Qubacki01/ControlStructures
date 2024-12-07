###
# Age check program
#

age = int(input('Enter your age: '))

if age > 0 and age < 13:
    age_group = 'Child'
elif age >= 13 and age < 20:
    age_group = 'Teen'
elif age >= 20 and age < 65:
    age_group = 'Adult'
elif age >= 65:
    age_group = 'Senior'
else:
    print('Invalid number! Cannot be below 0!')
    age_group = 'INVALID INPUT'

print(f'Your age group is: {age_group}')