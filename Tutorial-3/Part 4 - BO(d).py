#Initialization
marks = 0

#User Inputs
marks = int(input("Enter your marks - "))

#Process01
if marks < 0 or marks > 100:
    print("Invalid Mark, Enter again")
else:
    print("Valid Mark")

#Process02
if marks >= 70:
    print("Exceptional Mark")
elif marks >= 40:
    print("Satisfactory Result")
else:
    print("You have failed")
    