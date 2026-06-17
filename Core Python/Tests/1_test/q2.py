### 2. Write a program to calculate simple interest based on pricipal, Rate and Time.
# (SI = P*R*)T/ 100 )


# Take pricipal, Rate and Time as an input from the user
p = int (input("Enter the principal amount : "))
r = int (input("Enter the rate of interest (per years) : "))
t = int (input("Enter the time (in years) : "))

# Calculate the simple interest 
SI = p * r * t / 100 

# Display results
print( f"The Simple Interest = {SI}.")
