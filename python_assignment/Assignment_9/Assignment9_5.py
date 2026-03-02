def SQRT(a):
    if a % 3 == 0 :
        print(a,"is divisible by 3")
    else:
        print(a,"is not divisible by 3")
     
    
a = float(input("Enter first number: "))

result = SQRT(a)
print("The cube of", a, "is", result)