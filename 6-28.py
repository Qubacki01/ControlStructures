###
# Write a program that prints the first twenty words of the Fibonacci sequence.
#

terms = 20          # First to num
a = 0
b = 1

print(a, end=', ')      # First term

for i in range(terms - 1):      # loop 19 times
    print(b, end=', ')
    a, b = b, a + b