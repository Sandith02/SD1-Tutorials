#Inilialization
num1 = 0
num = 0
operator = 0
calculation = 0

#User Inputs
num1 = int(input("Enter first number - "))
operator = str(input("Choose prefered operator - "))
num2 = int(input("Enter second number - "))

#Process
if operator == "+":
    calculation = num1 + num2
    print(calculation)
elif operator == "-":
    calculation = num1 - num2
    print(calculation)
elif operator == "*":
    calculation = num1 * num2
    print(calculation)
elif operator == "**":
    calculation = num1 ** num2
    print(calculation)    
elif operator == "/":
    calculation = num1 / num2
    print(calculation)
else:
    print("Unknown Operator, Try Again")

    