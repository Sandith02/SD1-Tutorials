#Intialization
cost = 0
slevel = 0
tip = 0

#User Inputs
cost = int(input("Enter cost of the meal - "))

#Statements
print("*Let us know your satisfaction level*\n\n1 = Totally Satisfied\n2 = Satisfied\n3 = Dissatified\n" )

#User Inputs
slevel = int(input("Enter - "))

#Process
if slevel == 1:
    tip = cost * 20/100
elif slevel == 2:
    tip = cost * 15/100
elif slevel == 3:
    tip = cost * 10/100
else:
    print("Invalid Input")

#Output
print("\nTip is - ",tip)
