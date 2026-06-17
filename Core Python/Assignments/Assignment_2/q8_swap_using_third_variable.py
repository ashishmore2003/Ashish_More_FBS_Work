### 8. Write a Program to Swap Two Numbers Using a Third Variable

print("Before Swapping...!")

# Take first and second number as input from the user
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

# Swapping the numbers
temp = num1
num1 = num2
num2 = temp

# Display Result
print("After Swapping...!")

print(f"First Number : {num1}")
print(f"Second Number : {num2}")
