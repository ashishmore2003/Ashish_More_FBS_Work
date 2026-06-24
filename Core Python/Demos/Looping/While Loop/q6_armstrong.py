### Q6. To Comapare number is armstrong or not 

# Step 1 : Take number as an input from the user
num = int(input("Enter The Number : "))

# Step 2 : Store number in temp for calculations
temp = num 

# Step 3 : Initialize variable 
sum = 0 
count = 0 

# Step 4 : For separate digits 
while temp > 0 :
    digit = temp % 10 
    temp = temp // 10 
    count+=1

# Step 5 : Reset temp variable value
temp = num 

# Step 6 : Calculation for armstrong number 
while temp > 0 :
    digit = temp % 10 
    temp = temp // 10 
    sum = sum + digit ** count 

# Step 7 : Compare the number is armstrong or not 
if sum == num :
    print(f"The Number Is Armstrong : {num}")
else :
     print(f"The Number Is Not Armstrong : {num}")
