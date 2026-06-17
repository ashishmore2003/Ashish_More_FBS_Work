### 3. Program to Check Username and Password

# Store correct username
username = "ashu"

# Store correct password
password = "1234"

# Take username as input from user
user_name = input("Enter The Username: ")

# Take password as input from user
user_password = input("Enter The Password: ")

# Check username and password
if username == user_name and password == user_password:
    print("Logged in Successfully...!")
else:
    print("Invalid Credentials...!")
