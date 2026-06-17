### 8. Write a program to convert days into years, weeks and days.

# Take number of days as input from the user
days = int(input("Enter number of days: "))

# Calculate years
years = days // 365

# Remaining days after calculating years
remaining_days = days % 365

# Calculate weeks
weeks = remaining_days // 7

# Remaining days after calculating weeks
days_left = remaining_days % 7

# Display the result
print("Years =", years)
print("Weeks =", weeks)
print("Days =", days_left)
