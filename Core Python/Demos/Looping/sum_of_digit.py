### To print the sum of number from 1 to N.

# Take input from user
n = int(input("Enter the number: "))

# Initialize starting number
i = 1

# Variable to store total sum
sum = 0

# Run loop until i reaches n
while(i <= n):

    # Add current value of i into sum
    sum = sum + i

    # Increase i by 1
    i += 1

# Print final result
print(f"The sum of numbers from 1 to {n} is : {sum}")
