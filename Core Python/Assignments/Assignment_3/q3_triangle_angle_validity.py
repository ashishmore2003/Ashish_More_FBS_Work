# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

# Take three angle of triangle as an input from the user
a = int(input("Enter First Angle : "))
b = int(input("Enter Second Angle : "))
c = int(input("Enter Third Angle : "))

# Addition of three angle of tringle 
triangle = a + b + c

# To Check The Triangle Is Valid Or Not Valid 
if triangle > 0 and triangle <= 180:
    print("Triangle is valid")
else:
    print("Triangle is not valid ")
    