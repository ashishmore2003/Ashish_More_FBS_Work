# 5. Write a program to check whether the triangle is equilateral,
# isosceles or scalene triangle.

# Take all three sides as input from the user
side1 = float(input("Enter Side 1 : "))
side2 = float(input("Enter Side 2 : "))
side3 = float(input("Enter Side 3 : "))

# Check whether triangle is valid or not
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):

    # Check for Equilateral
    if side1 == side2 == side3:
        print("Equilateral Triangle")

    # Check for Isosceles
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles Triangle")

    # Otherwise Scalene
    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")
    