### 6. Write a program to calculate profit or loss.

# Take Cost Price and Selling Price as input from the user
cp = int(input("Enter the Cost Price: "))
sp = int(input("Enter the Selling Price: "))

# Calculate the difference between Selling Price and Cost Price
amount = sp - cp

# Check whether profit, loss, or no profit-no loss
if amount > 0:
    print(f"Profit is Rs.{amount}")

elif amount == 0:
    print("No Profit, No Loss")

else:
    print(f"Loss is Rs.{abs(amount)}") 
    
# Note: abs() is absolute function: convert number into positive
