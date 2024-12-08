###
#
#

amount = int(input("Enter the amount in PLN: "))

five_pln = amount//5
rem_amount = amount % 5

two_pln = rem_amount// 2
rem_amount = rem_amount % 2

one_pln = rem_amount

# Print the result
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")
