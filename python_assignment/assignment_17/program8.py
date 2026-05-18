def DesignPrint(iNo):
    for i in range (iNo):
        for j in range(i):
            print(i ,end ="")
        print()
            
def main():
    iNos = int(input("Enter the nos "))
    DesignPrint(iNos)
    
main()
    