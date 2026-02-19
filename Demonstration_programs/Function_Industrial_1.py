#Procedural programming 
def CheckEven(No):
    if(No % 2 == 0 ):
        return True
    else:
        return False
def main ():
    No = 0
    ret = False
    No = int(input("Enter the nos to e checked:"))              
    ret = CheckEven(No)
    if (ret == True):
        print("It is even ")
    else:
        print("It is false")
if(__name__ == "__main__"):                         
    main()







