### 4. WAP to calculate area of triangle and rectangle

# Take base of triangle as input from user.
base = float(input("Enter Base of Triangle: "))

# Take height of triangle as input from user.
height = float(input("Enter Height of Triangle: "))

# Calculate area of triangle,
triangle_area = 0.5 * base * height

# Take length of rectangle as input from user.
length = float(input("Enter Length of Rectangle: "))

# Take width of rectangle as input from user.
width = float(input("Enter Width of Rectangle: "))

# Calculate area of rectangle.
rectangle_area = length * width

# Display Result.
print("Area of Triangle:", triangle_area)
print("Area of Rectangle:", rectangle_area)
