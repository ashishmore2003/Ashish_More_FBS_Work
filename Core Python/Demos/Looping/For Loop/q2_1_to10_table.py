# Write a Python program to accept a number from the user 
# and print its multiplication table from 1 to 10 using a for loop.


# Take a number as input from the user
n = int(input("Enter the number : "))

# Loop from 1 to 10 to generate multiplication table
for i in range(1, 11):

    # Print multiplication in table format
    print(f"{n} * {i} = {i*n}")
    