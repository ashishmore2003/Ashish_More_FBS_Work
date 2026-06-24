# Write a program to accept a number from the user and check whether it is a Perfect Number or not.

# A Perfect Number is a number whose sum of proper divisors (excluding itself)
# is equal to the number itself. Example: 6 → 1 + 2 + 3 = 6

# Take number as input from user
num = int(input("Enter the number : "))

# Variable to store sum of divisors
sumDivisor = 0

# Loop from 1 to one number before the input number
for i in range(1, num):

    # Check if i is divisor of num
    if num % i == 0:

        # Add divisor into sum
        sumDivisor = sumDivisor + i

# Check if sum of divisors equals original number
if sumDivisor == num:

    # Number is perfect
    print(f"{num} Is Perfect Number.")

else:

    # Number is not perfect
    print(f"{num} Is Not Perfect Number.")
