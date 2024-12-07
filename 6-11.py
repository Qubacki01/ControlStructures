###
# A computer program analyses the price of a product in an online store. 
# If the product price decreases by at least 10%, 
# the program prints a purchase recommendation.
#

past_price = int(input('Enter previous product price: '))
current_price = int(input('Enter current product price: '))
price_red_calc = (1-current_price/past_price)*100
price_redux = f'{price_red_calc:.2f}'

if price_red_calc >= 10:
    print('Buy the product!')
    print(f'Product price reduced by {price_redux}%')
else:
    print('Price unchanged')
