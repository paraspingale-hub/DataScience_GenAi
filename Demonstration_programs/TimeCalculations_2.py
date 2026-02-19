#understanding the concept of PID
import time                                            
def Factorial(no):
    fact = 1
    for i in range (1,no+1):
        fact = fact * i
    return fact

def main ():
    starttime = time.time()
    value  = int (input("Enter the nos "))
    ret = Factorial(value)
    print("Factorial of the no is :",ret)
    endtime = time.time()

    print("total execusion time is :" , endtime - starttime)


    
if __name__ == "__main__":
    main()