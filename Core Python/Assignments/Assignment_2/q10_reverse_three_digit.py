### 10. Write a program to reverse three-digit number.

# Take three digit number as input from the user 
num = int(input("Enter Three Digit Number : "))

# Extract the three digit number 
d1 = num % 10 
num = num // 10

d2 = num % 10 
num = num // 10

d3 = num % 10 
num = num // 10

# Reverse the three digit number
reverse = (d1 * 100) + (d2 * 10) + (d3)

print("Reversed Number : ",reverse)