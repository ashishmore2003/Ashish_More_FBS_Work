# 7. Write a program to check if user has entered correct userid and password.

# Store correct userid and password
correct_userid = "admin"
correct_password = "12345"

# Take input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Check userid and password
if userid == correct_userid and password == correct_password:

    # Login successful
    print("Login Successful")

else:

    # Login failed
    print("Invalid User ID or Password")
    