### Q5. To calculate total numaber of digits 

# Take number as an input from the user 
num = int(input("Enter Number : "))

# Store original number in temp variable
temp = num

# Variable to count digits
count = 0

# Run loop until number becomes 0
while temp > 0:

    # Extract last digit
    digit = temp % 10

    # Remove last digit
    temp = temp // 10

    # Increase digit count
    count = count + 1

# Display total number of digits
print(f"Total Number Of Digits : {count}")
