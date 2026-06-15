### 5. Write a program to enter P, T, R and calculate Compound Interest.

# Take principal amount as input from the user
p = float(input("Enter Principal Amount: "))

# Take rate of interest as input from the user
r = float(input("Enter Rate of Interest: "))

# Take time in years as input from the user
t = float(input("Enter Time (in years): "))

# Calculate compound interest
ci = p * ((1 + r / 100) ** t) - p

# Display the compound interest
print("Compound Interest =", ci)
