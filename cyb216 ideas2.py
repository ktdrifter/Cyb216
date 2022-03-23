#strong password detection

# Import regular expression module (it's required to run regex)
import re

# Print all the password criteria for a strong password
print('\nA strong password consists of: \nA total of at least 8 characters, 1 capital letter, 1 lowercase letter, 1 number, and 1 special character!')

print ("\n*Type 'goodbye' to close")

token = 1

while token == 1:

    # Ask user to input their password and set user_password variable to their input
    user_password = input('\nEnter a password to verify its strength: ')

    # Ending the program

    if user_password == 'goodbye':

        token -= 1

    # if statement to verify the users input matches the criteria of a strong password and print that the password is strong, otherwise print the password is not strong
    # re.match will define a pattern of specified criteria to be matched, then we will pass the user input to match against the regex pattern
    # Use re.match because we want our defined criteria to be match against the user_password string
    # Each set of criteria is specified within each set of paranthesis
    # ?= is a positive lookahead. This ensures the entire string is searched then matched for each set of criteria. We need this so that any combination of characters can be searched rather than finding a match in the middle of the string and only matching from there on.
    # .* means we can match 0 or more characters of any type (although we will specify the character range for each set of criteria
    # The range of characters in the [ ] define each set of criteria (e.g. [A-Z] matches capital letters while [0-9] matches digits). There are code such as /w or /d that we can use but I think it's more clear to put the actual range of the characters in this case.
    # The {2} within each set of paranthesis makes it so that we search for each set of criteria twice as we are requiring the user to have 2 capital letters, 2 lowercase, etc.
    # The special character criteria is defined manually by typing out all of the special characters to match. ***NOTE: If a user types a special character that's not defined here it will not match and tell them their password is not strong
    # The .{8,} means match any character for a minimum of 8 characters with no maximum amount of characters (this is how we meet the criteria for 8 character minimum)
    # Each set of criteria was tested individually before being combined into one statement
    # The site https://regex101.com is very useful for learning regex and validating input

    elif re.match('(?=.*[A-Z]{1})(?=.*[a-z]{1})(?=.*[0-9]{1})(?=.*[!@#$%^&*()?<>_+=]{1}).{8,}', user_password):

        # If match is found then print message telling user password is strong
        print('Password IS STRONG!')

        # Since the password is strong, the user's objective is complete, setting the resume variable to anything other than 'true' will end the loop
        resume = 'false'

    # else statement, ALL defined password criteria must match, otherwise tell user their password is not strong enough
    else:
        print('Password is not strong enough - Try Again!')


print ("\nThank you for using our program! Please come again!")
