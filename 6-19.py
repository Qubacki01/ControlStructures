###
# Write a program that prints a survey consisting of three questions.
#

cats = input("Do you like cats? (y/n): ") == 'y'
pancakes = input("Do you like pancakes? (y/n): ") == 'y'
pancake_cats = input("Do you have a pancake cat? (y/n): ") == 'y'

print("SURVEY RESULTS")
print(f"Likes a cat: {'Yes' if cats else 'No'}")
print(f"Likes pancakes: {'Yes' if pancakes else 'No'}")
print(f"Has a pancake cat: {'Yes' if pancake_cats else 'No'}")
