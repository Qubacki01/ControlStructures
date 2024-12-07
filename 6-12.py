###
#In one of the online stores, a 25% discount is charged 
# for each product purchased over two. Write a program 
# that calculates the amount to be paid. Read the number of 
# purchased products and the product price from the keyboard
#

number_of_products = int(input('Enter number of products: '))
unit_price = int(input('Enter price: '))

if number_of_products > 2:
    price = 2*unit_price + (number_of_products - 2) * unit_price * 0.75
else:
    price = number_of_products * unit_price


print(f'Number of products purchased: {number_of_products}')
print(f'Product price: {unit_price}')
print(f'Amount to pay: {price}')