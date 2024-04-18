#Tip Calculator Python Program!
"""
Each person should pay (150 / 5) * 1.12 = 33.6
1.Bill
2.people
3.tip %
Format the result to 2 ways to round a number-
"""
bill = float(input("Inserta el monto total a pagar: "))
tip =  int(input("How much tip would you like to give? 10,12 or 15 "))
people = int(input("How many to split the bill?  "))
bill_with_tip = (tip / 100) * bill + bill
bill_div_people= bill_with_tip/people
final_amount= round(bill_div_people,2)
print(f"La factura de : ${bill} la vamos a dividir entrea {people} personas y nos tocaria pagar a cada uno ${final_amount}  ")
