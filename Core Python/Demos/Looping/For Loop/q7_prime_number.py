### To print the prime number by using flag 

# way 1 :

# num = int (input("Enter the number : "))
# flag = 0
# if num >= 2:
#     for i in range(2,num):
#         if num % i == 0 :
#             flag = 1
#             break
#     if flag == 0:
#         print(f"{num} number is prime ")
#     else :
#         print(f"{num} number is not prime ")
# else :
#     print("The given number is not eligible to cheking is prime or not ")

# Way 2 :

num = int (input("Enter the number : "))

if num <=1:
        print("The given number is not eligible to cheking is prime or not ")
else:
    for i in range(2,num):
        if num % i == 0 :
           print(f"{num} number is not prime ")
           break
    else:
        print(f"{num} number is prime ")
    