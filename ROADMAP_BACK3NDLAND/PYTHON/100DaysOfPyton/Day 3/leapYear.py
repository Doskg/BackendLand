print("Today we are going to create a Leap Year calculator..!!")

print("The leap year contains 366 days.")
year = int(input("Insert the year: "))
if year % 4 == 0:
    print(f"the year {year} is a leap year.!!")
else:
    print(f"the year {year} is not a leap year.!!")
