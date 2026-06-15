### 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Take marks of five subjects as input from the user
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

# Total maximum marks
max_marks = 500

# Calculate total obtained marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = (total / max_marks) * 100

# Display total marks and percentage
print("Total Marks =", total)
print("Percentage =", percentage, "%")
