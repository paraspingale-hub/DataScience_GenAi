def SQRT(a):
    sqrt = a * a * a
    return sqrt
     
    
a = float(input("Enter first number: "))

result = SQRT(a)
print("The cube of", a, "is", result)