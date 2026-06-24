# WAP to demonstrate the use of continue statement with for loop and else block

# Loop starts from 1 and goes till 9 (10 is excluded)
for i in range(1, 10):

    # Check if i becomes 7
    if i == 7:
        continue   # Skip current iteration (7 will not be printed)

        # break   # If used instead of continue, loop will stop at 7

    else:
        # Print numbers except skipped values
        print(i)

# This else runs after loop completes normally
else:
    print("Loop is executed succesfully")
