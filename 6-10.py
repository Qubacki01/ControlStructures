###
# Dog age to human age calculator
#

dog_human_age = int(input("Enter dog's age: "))

if dog_human_age <= 2:
    dog_years = dog_human_age*10.5
elif dog_human_age > 2:
    dog_years = 2*10.5 + (dog_human_age - 2)*4

print(f"The dog's age in dog years is {dog_years}")

