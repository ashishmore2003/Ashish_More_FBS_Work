# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Take marks of 5 subjects from user
sub1 = float(input("Enter Subject 1 Marks: "))
sub2 = float(input("Enter Subject 2 Marks: "))
sub3 = float(input("Enter Subject 3 Marks: "))
sub4 = float(input("Enter Subject 4 Marks: "))
sub5 = float(input("Enter Subject 5 Marks: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = total / 5

# Display grade
if percentage >= 75:
    print("Distinction")

elif percentage >= 60:
    print("First Class")

elif percentage >= 50:
    print("Second Class")

elif percentage >= 35:
    print("Pass Class")

else:
    print("Fail")
