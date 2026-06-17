# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

# Import random module
import random

# Store correct userid and password
correct_userid = "admin"
correct_password = "12345"

# Take input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Verify userid and password
if userid == correct_userid and password == correct_password:

    # Generate random 4-digit number
    captcha = random.randint(1000, 9999)

    # Display captcha
    print("Captcha:", captcha)

    # Take captcha input
    user_captcha = int(input("Enter the same captcha: "))

    # Verify captcha
    if user_captcha == captcha:
        print("Login Successful")

    else:
        print("Captcha Verification Failed")

else:
    print("Invalid User ID or Password")

