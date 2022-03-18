#strong password detection

#if? #find special character
    #search for uppercase
        #search for number
            #search for 16 characters
            #print  success!

# Print all the password criteria for a strong password
print('\nA strong password consists of: \nA total of at least 8 characters, 2 capital letters, 2 lowercase letters, 2 numbers, and 2 special characters!')

print ("\n*Type 'goodbye' to close")

token = 1

while token == 1:

    spec_char = ['!', '@', '#', '$', '%', '^', '*', '+', '?', '~', '-', '_', '.', ',']

    password = input ("\nPlease make a strong password: ")

    if password == 'goodbye':

        token -= 1

    elif '!' in password:

        print ('\nThis IS a strong password!')

    else:

        print ('\nThis is NOT a strong password!')

print ("\nThank you for using our program! Please come again!")
