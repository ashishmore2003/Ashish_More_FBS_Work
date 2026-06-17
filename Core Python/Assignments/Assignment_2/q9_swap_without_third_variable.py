### 9. Write a program to swap two numbers without using third variable.

print("Before Swapping...!")

# Take first and second number as input from the user
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

# Swapping the numbers
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2 

# Display Result
print("After Swapping...!")

print(f"First Number : {num1}")
print(f"Second Number : {num2}")
