num = (input("Enter your phone number: "))  
num = list(num)   
if len(num) == 10 and (num[0]== '9' or num[0]== '8' or num[0]== '7') :  
    print("Valid number")
else:
    print("Invalid number")
