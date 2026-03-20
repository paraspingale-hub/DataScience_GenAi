def Displaydigits(no):
    digit = 0
    while(no != 0):
        digit = no % 10
        print(digit)
        no = no // 10
        
        
    
def main ():
    no = 0
    print("Enter the nos")
    no = int(input())
    Displaydigits(no)
    
    
main()
