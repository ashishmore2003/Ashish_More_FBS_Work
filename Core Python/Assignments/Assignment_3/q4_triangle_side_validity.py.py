# Write a program to check whether triangle is valid or not

# Take all three sides as input from the user
side1 = float(input("Enter Side 1 : "))
side2 = float(input("Enter Side 2 : "))
side3 = float(input("Enter Side 3 : "))

# Check triangle validity
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Triangle is Valid")
    
else:
    print("Triangle is Not Valid")