### 6. Write a Program to input two angles from user and find third angle of the triangle.

# Take first angle as input from the user
angle1 = float(input("Enter first angle: "))

# Take second angle as input from the user
angle2 = float(input("Enter second angle: "))

# Calculate the third angle
angle3 = 180 - (angle1 + angle2)

# Display the third angle
print("Third Angle =", angle3)
