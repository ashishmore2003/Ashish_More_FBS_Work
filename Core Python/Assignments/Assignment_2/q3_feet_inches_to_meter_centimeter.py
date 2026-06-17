### 3. Convert Distance Given in Feet and Inches into Meter and Centimeter

# Take feet as input from user
feet = float(input("Enter Distance in Feet: "))

# Take inches as input from user
inches = float(input("Enter Distance in Inches: "))

# Convert feet to meter
meters = feet * 0.3048

# Convert inches to centimeter
centimeters = inches * 2.54

# Display Result
print(f"Distance in Meters: {meters}")
print(f"Distance in Centimeters: {centimeters}")
