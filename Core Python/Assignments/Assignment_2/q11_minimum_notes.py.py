### 11. Write a program to accept an integer amount from user 
# and tell minimum number of notes needed for representing that amount.

# Take amount as an input from the user 
amount = int(input("Enter The Amount : "))

# Perfrom operations for minimum number of notes

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

notes_5 = amount // 5
amount = amount % 5

notes_2 = amount // 2
amount = amount % 2

notes_1 = amount // 1
amount = amount % 1 

print("THE NOTES :")
print(f"Notes of 500 : {notes_500}")
print(f"Notes of 200 : {notes_200}")
print(f"Notes of 100 : {notes_100}")
print(f"Notes of 50 : {notes_50}")
print(f"Notes of 20 : {notes_20}")
print(f"Notes of 10 : {notes_10}")
print(f"Notes of 5 : {notes_5}")
print(f"Notes of 2 : {notes_2}")
print(f"Notes of 1 : {notes_1}")
