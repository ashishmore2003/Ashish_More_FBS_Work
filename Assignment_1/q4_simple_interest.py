### 4. Write a program to enter P, T, R and calculate simple Interest.

# Take principal amount as input from the user
p = float(input("Enter Principal Amount: "))

# Take rate of interest as input from the user
r = float(input("Enter Rate of Interest: "))

# Take time in years as input from the user
t = float(input("Enter Time (in years): "))

# Calculate simple interest
si = (p * r * t) / 100

# Display the simple interest
print("Simple Interest is : ", si)
