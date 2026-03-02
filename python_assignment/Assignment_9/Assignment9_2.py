def GRTCheck(a,b):
    if a>b:
        print(a,"is greater than",b)
    elif a<b:
        print(a,"is less than",b)
    else:
        print(a,"is equal to",b)    
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
GRTCheck(a,b)