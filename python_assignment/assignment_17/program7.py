def DesignPrint(iNo):
    for i in range (iNo):
        for j in range(iNo):
            print(j ,end ="")
        print()
            
def main():
    iNos = int(input("Enter the nos "))
    DesignPrint(iNos)
    
main()
    