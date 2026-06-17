# 1. Write a program to accept amount and tell minimum number of notes needed

try:

    # Take input
    amount = float(input("Enter The Amount : "))

    # For Input validation
    if amount <= 0 or amount != int(amount):
        print("Invalid Amount")

    else:

        amount = int(amount)

        if amount >= 500:
            notes_500 = amount // 500
            amount = amount % 500
            print(f"Notes of 500 : {notes_500}")

        if amount >= 200:
            notes_200 = amount // 200
            amount = amount % 200
            print(f"Notes of 200 : {notes_200}")

        if amount >= 100:
            notes_100 = amount // 100
            amount = amount % 100
            print(f"Notes of 100 : {notes_100}")

        if amount >= 50:
            notes_50 = amount // 50
            amount = amount % 50
            print(f"Notes of 50 : {notes_50}")

        if amount >= 20:
            notes_20 = amount // 20
            amount = amount % 20
            print(f"Notes of 20 : {notes_20}")

        if amount >= 10:
            notes_10 = amount // 10
            amount = amount % 10
            print(f"Notes of 10 : {notes_10}")

        if amount >= 5:
            notes_5 = amount // 5
            amount = amount % 5
            print(f"Notes of 5 : {notes_5}")

        if amount >= 2:
            notes_2 = amount // 2
            amount = amount % 2
            print(f"Notes of 2 : {notes_2}")

        if amount >= 1:
            print(f"Notes of 1 : {amount}")

except:
    print("Invalid Input")
