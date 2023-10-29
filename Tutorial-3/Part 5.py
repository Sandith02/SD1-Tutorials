#Initilization
response = 0

#User Inputs.
response = str(input("Do you like python(Yes/No) : ")).lower()

#Process
if response == 'yes' or response == 'y':
    print("you are on the right course")
elif response == 'no' or response == 'n':
    print("you might change your mind") 
else:
    print("I did not understand")


