### 2. Write a program to input any alphabet and check whether it is vowel or consonant.

# Take a alphabet as input from user
alpha = input("Enter the alphabets lettes :")


if alpha in 'aeiouAEIOU':
    print(f"{alpha} is vowel.")
else:
    print(f"{alpha} is Consonants.")