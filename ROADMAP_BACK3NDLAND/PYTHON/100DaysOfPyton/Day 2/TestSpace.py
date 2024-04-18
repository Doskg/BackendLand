
""" 

c=int(input("Ingresa tu edad: "))

if c==1 and c<18:
  print("Eres menor de edad")
else:
  print("Eeres mayor de edad")
  
"""


"""
-Data Types
-Numbers
-Operations
-Type Conversion
-f-Strings

"""
#print(Len("hello")--> 4


#Data Types 
#Strings "Hello" [0]
# print("Hello" [0])

# #Integer
# primt(123+123)

# #Float
# print(3.2)

# #Boolean
# print(True, False)

# #len() Does not like to work with Int
# num_char= len(input("Hello World"))
# print("Your name has " + num_char + "characters.")


# b = float(1)
# a = "234"
# print(f"el dato {b} + {a} es igual {float(a)+ b}")
""""

#1st input, enter height in meters e.g. 1.65
height=float(input("Insert your own height: "))
#2nd input, enter weight in kilograms e.g: 72
weight=float(input("Insert your own weight: "))

BMI=weight/height**2
print(f"Your BMI is {BMI}")

print(round(2.6666666666, 2))
print(type(8//3))

result = 4/2
print(result)

#user scores a point

# score +=1
score=0
height = 1.8
isWinning = True

#print("Your score is " + str(score))
#Avoiding to convert every data type to a string
#---------f-string-----------
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")
"""
################################
#-------Challenge------------#
#Life in weeks 90 years is the Goal
age=int()
goal=int()
age=input('Insert your age: ')
years=90-int(age)
year_weeks=years*52

print(f"You have {year_weeks} weeks left")




