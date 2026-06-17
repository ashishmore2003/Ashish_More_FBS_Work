### 6. WAP to calculate total salary of employee based on basic,
# da=10% of basic,ta=12% of basic, hra=15% of basic.

# Take basic salary as input from user 
basic_salary = int(input("Enter Your Basic Salary : "))

# Calculate DA as 10% of Basic Salary.
da = (basic_salary * 10 / 100)

# Calculate TA as 12% of Basic Salary.
ta = (basic_salary * 12 / 100)

# Calculate HRA as 15% of Basic Salary.
hra = (basic_salary * 15 / 100)

# Calculate Total Salary.
Total_Salary = basic_salary + da + ta + hra

# Display Result.
print("Total Salary : ",Total_Salary)
