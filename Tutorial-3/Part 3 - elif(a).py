#Initialization
temp = 0
num = 0
ftemp = 0
ctemp = 0

#Statements
print("Enter '1' for Celsius to Fahrenheit Conversion - \nEnter '2' for Fahrenheit to celcius conversion - \n\n")

#User Inputs
num = int(input("Enter Number -  "))

#Process
if num == 1:
    print("You selected the Celsius to Fahrenheit Conversion")
    temp = int(input("Enter temperature in Celsius - "))
    ftemp = (ctemp * 1.8) + 32
    print("Converted temperature - ",ftemp)
elif num == 2:
    print("You selected the Fahrenheit to Celsius Conversion")
    temp = int(input("Enter temperature in Fahrenheit - "))
    ctemp = (ftemp -32 ) / 1.8
    print("Converted temperature - ",ctemp)
else:
    print("Invalid Input")
