# Write a program to accept starting and ending values from the user 
# and print all odd numbers between that range using a for loop.

# Take starting and ending number from user
a = int(input("Enter start:"))
b = int(input("Enter end:"))

# Print blank line for better output formatting
print()

# Display heading
print('Odd Numbers : ')

# Loop from start value to end value
for i in range(a, b + 1):

    # Check if number is odd
    if i % 2 != 0:

        # Print odd number
        print(i)
