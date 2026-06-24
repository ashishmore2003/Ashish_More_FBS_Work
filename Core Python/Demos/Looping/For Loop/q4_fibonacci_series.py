### Write a program to generate Fibonacci series.

# Take number of terms from user
n = int(input("Enter the number : "))

# Initialize first two values
a = -1
b = 1

# Loop n times to generate Fibonacci series
for i in range(n):

    # Generate next number
    c = a + b

    # Update values for next iteration
    a = b
    b = c

    # Print current Fibonacci number
    print(c)
