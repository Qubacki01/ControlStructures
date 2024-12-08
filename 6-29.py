###
# A natural number greater than 1 is called a prime if it has exactly 2 
# natural factors with the values 1 and this number. 
# Write a program that finds N leading prime numbers. 
# Read the value of N from the keyboard. Using loop statements check that 
# the number N is divisible only by 1 and by N.
#

n = int(input("Enter the number of prime numbers to find: "))

primes = []
num = 2

while len(primes) < n:
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):   # all - is everythinf true
        primes.append(num)
    num += 1

print("Prime numbers:", *primes)
