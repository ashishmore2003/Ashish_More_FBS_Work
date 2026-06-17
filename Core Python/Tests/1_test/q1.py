### 1. Write a program to find the area and parimeter of following figure (Accept the length, breadth and radius from user)
 
# Take input from the user
redius = int(input("Enter the radius :"))
length = int(input("Enter the length :"))
breadth = int(input("Enter the breadth :"))

### FIND THE AREA OF FIGURE.

# Find the without one side breadth area of rectangle of figure 
rect_area = length * breadth 

# Find the half circle area of figure 
half_circle_area = (3.14 * redius * redius) / 2

# Find the Final complete are of figure (without one side breadth area of rectangle + half circle area)
final_area = rect_area + half_circle_area 

### FIND THE PERIMETER OF FIGURE.

# Find the without one side breadth perimeter of rectangle of figure 
rect_perimeter =(2 * length) + breadth 

# Find the half circle perimeter of figure 
half_circle_perimeter = 3.14 * redius 

# Find the Final complete perimeter of figure (without one side breadth perimeter of rectangle + half circle perimeter)
final_perimeter = rect_perimeter + half_circle_perimeter

# Dispaly result 
print(f"The final area is : {final_area}")
print(f"The final perimeter is : {final_perimeter}")

