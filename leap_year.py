# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year % 4 == 0  or year % 100 == 0  and year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


if year % 4 == 0:
    if year % 100:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        ("Leap Year.")
else:
    print("Not a Leap Year.")