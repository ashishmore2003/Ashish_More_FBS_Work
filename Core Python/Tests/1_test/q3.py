### 3. Write a program to accept distance in km and convert it into meters and centimeters both.

# Take distance in km as an input from the user
km = int(input("Enter the distance in kilometers : "))

# Convert the km distance in meters 
mm = km * 1000 

# convert the meter distance into centimeters 
cm = mm * 100

# Display the result 
print(f"Distance in meters : {mm} m")
print(f"Distance in centimeters : {cm} cm")
