### 3. Write a program to check Mail and Femail is eligible for marriage and or not.

# Take gender input from user
gender = input("Enter Gender (M/F): ")

# Check if entered gender is valid
if gender == 'M' or gender == 'F':

    # Take age input only if gender is valid
    age = int(input("Enter Age: "))

    # Check for Female eligibility
    if gender == 'F':
        if age >= 18:
            print("Girl is eligible for marriage.")
        else:
            print("Girl is not eligible for marriage.")

    # Check for Male eligibility
    else:
        if age >= 21:
            print("Boy is eligible for marriage.")
        else:
            print("Boy is not eligible for marriage.")

# If user enters anything except M/F
else:
    print("Invalid Gender! Please enter only M or F.")
