###
# The speed of vehicles on highways in Poland is at least 40 km/h
#  and not more than 140 km/h. Write a program that prints a
#  message when the specified car speed, read from the keyboard,
#  has been exceeded.
#

car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed >= 40 and car_speed <= 140:
    print()
elif car_speed < 40:
    print('! Invalid car speed !')
else:
    print('! Speed limit exceeded !')