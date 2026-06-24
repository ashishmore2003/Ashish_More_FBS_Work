### Q3. Write a Python program to accept a number from the user and 
#       print each digit of the number separately using a while loop.


# Take number as an input from the user
num = int(input("Enter Number : "))

# Store original number in temp variable
temp = num

# Run loop until all digits are processed
while temp > 0:

    # Extract last digit
    digit = temp % 10

    # Remove last digit from number
    temp = temp // 10

    # Print separated digit
    print(f"Seprate Digits : {digit}")
