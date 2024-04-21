print("****** PIZZA ORDER ********")
print("//Thank you for choosing Python Pizza deliveries!!//")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra Cheese Y or N : ")
bill = 0
if size == "s":
    bill = 15
    print("Small Pizza : $15")
elif size == "m":
    bill = 20
    print("Medium Pizza : $20")
elif size == "l":
    bill = 25
    print("Large Pizza : $25")
else:
    print("Error!!")
if add_pepperoni == "y":
    bill = bill + 3
    print(f"adding $3 to your order for the extra pepperoni")
else:
    print("No extra Pepperoni")
if extra_cheese == "y":
    bill = bill + 1
    print(f"adding $1 to your order for the extra cheese")
else:
    print("No extra Cheese.!")

print(
    f"Thank you for choosing Python Pizza Deliveries!, The total bill for your {size} Size  is : ${bill}"
)
"""
Other solution

if size == "S":
    bill = 15
elif size == "M":
    bill=20
else:
    bill=25
if add_pepperoni == "y":
    bill=bill+3
else: 
    print("No extra Pepperoni")
if extra_cheese == "y":
    bill=bill+1
else: 
    print("No extra Cheese.!")
    
print(f"Thank you for choosing Python Pizza Deliveries!, Your final bill is : ${bill}.")   
    """
