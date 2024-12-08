###
# Write a program that prints a lottery coupon (numbers from 1 to 49).
#

for row in range(7):                # Rows
    for col in range(7):            # Columns
        number = row + col * 7 + 1  # num for pos
        print(number, end=' ')      # Print space, not new line
    print()                         #n New line
