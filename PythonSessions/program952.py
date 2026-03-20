def SumDigit(no):
    digit = 0
    isum = 0
    while(no != 0):
        digit = no % 10
        no = no / 10        
        isum = isum + digit
    return isum
def main ():
    no = 0
    print("Enter the nos")
    int(input())
    ret = SumDigits(no)
    print(ret)
    
    
main()
