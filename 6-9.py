###
# A program that prints the entered name 
# provided it is a female name
#

name = input('Enter name: ')

if name[-1] == 'a' or name[-1] == 'A':      # Can do with "name.endswith('a')"
    print(f'{name} -- Polish female name')
else:
    print('Not a Polish female name')

