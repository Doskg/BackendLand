print("******Welcome to the rollercoaster..!!*****")
height = int(input("Insert your height in cm.!    "))
if height > 120:
    print("*****You can ride the rollercoaster.!********")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif  age >=45 and age <=55:
        bill = 12
        print("Adults tickets are $12")
    else:# else is optional
        bill = 0
        print("Senior citizens tickets are free")
    wants_photo = input("Do you want a photo taken? Y or N:  ")
    if wants_photo == "y":
        # add $3 to their bill
        bill += 3
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")

else:
    print("******Sorry, You have to grow taller before you can ride.*******")

