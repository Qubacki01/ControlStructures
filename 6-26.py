###
# Write a program that checks if the PIN code entered in the payment 
# terminal is correct. The user has up to three possibilities for 
# entering a PIN code. In case of three unsuccessful attempts, the card is blocked.
#

pin = "6969"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter the PIN code: ")
    
    if entered_pin == pin:
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect...")
        
if attempts == 3:
    print(" ]*x*[ Sorry, your payment card has been blocked. ]*x*[ ")
