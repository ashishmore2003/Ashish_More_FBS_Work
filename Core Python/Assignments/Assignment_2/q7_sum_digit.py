### 6. WAP to Calculate the Sum of Digits of a Three-Digit Number

# Take a three-digit number as input from user
num = int(input("Enter a Three-Digit Number: "))

# Extract digits
digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10
num = num // 10

# Calculate sum of digits
sum_digits = digit1 + digit2 + digit3

# Display result
print("Sum of Digits:", sum_digits)
