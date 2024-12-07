###
# EAN-13 (European Article Number) is a barcode for marking goods.
# The first 3 digits (590) usually indicate goods manufactured in Poland.
# Write a program that checks whether the EAN-13 number entered from
# the keyboard consists of exactly 13 characters (digits). Print a 
# message if the number is correct. Additionally, only when the article 
# number is correct, print a message when the product was manufactured in Poland.
#

ean = input('Enter EAN-13 article number: ')

if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')

    if ean[0:3] == "590":
        print('Article is manufactured in Poland')
else:
    print('Invalid EAN number')