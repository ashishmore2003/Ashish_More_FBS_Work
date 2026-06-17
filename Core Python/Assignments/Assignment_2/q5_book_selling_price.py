### 5. WAP to Calculate Selling Price of a Book Based on Cost Price and Discount

# Take cost price as input from user
cost_price = float(input("Enter Cost Price of Book: "))

# Take discount percentage as input from user
discount = float(input("Enter Discount Percentage: "))

# Calculate discount amount
discount_amount = (cost_price * discount) / 100

# Calculate selling price
selling_price = cost_price - discount_amount

# Display Result
print("Selling Price of Book:", selling_price)
