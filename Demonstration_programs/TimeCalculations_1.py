#understanding the concept of PID
import os                                                
def Factorial(no):
    fact = 1
    for i in range (1,no+1):
        fact = fact * i
    return fact

def main ():
    value  = int (input("Enter the nos "))
    ret = Factorial(value)
    print("Factorial of the no is :",ret)
    
if __name__ == "__main__":
    main()