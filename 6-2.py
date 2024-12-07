###
# Counts vowels in the text
#
text = input("Enter text here: ")
vowels = "aeiouyAEIOUY"
vowel_count = 0
index = 0

# Count vowels in the text
while index < len(text):
    char = text[index]
    if char in vowels:
        vowel_count += 1
    index += 1      # Increase index to move to next character

print(f"The number of vowels in the text is: {vowel_count}")