# 12. Write a program to check if given 3 digit number is a palindrome or not.

# Take input from user
num = int(input("Enter a 3 Digit Number: "))

# Extract digits
first = num // 100
last = num % 10

# Check palindrome
if first == last:
    print("Palindrome Number")

else:
    print("Not a Palindrome Number")