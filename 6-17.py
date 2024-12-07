###
# Write a program that allows you to convert time in 24-hour 
# format to 12-hour format. The time in 24-hour format (hh:mm) 
# is read from the keyboard.
#

time_24 = input('Enter time (24-hour format): ').strip()

hrs, min = map(int, time_24.split(':'))  # split and convert into integers

if hrs >= 12:
    if hrs > 12:
        hrs -= 12
    suffix = 'PM'
elif hrs > 0 and hrs < 12:
    suffix = 'AM'
else:
    if hrs == 0:
        hours = 12
    suffix = 'AM'

time_12 = f"{hrs}:{min:2d}{suffix}"

print(f'Time in 12-hour format: {time_12}')