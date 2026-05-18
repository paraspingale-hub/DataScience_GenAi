def DesignPrint(iNo):

    for i in range(iNo , 0 , -1):
        iNo = iNo-1
        for j in range(iNo):
            print("#" ,end ="")
        print()
            
def main():
    iNos = int(input("Enter the nos "))
    DesignPrint(iNos)
    
main()
    