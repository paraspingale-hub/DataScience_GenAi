# Accept: Multi Parameters
# Return: 1 Parameter
def Marvellous1(Value1 ,Value2):  #positional argument
    print("Inside MArvellous1:" , Value1 , Value2)
    return 11 
def main (): 
    Result = None 
    Marvellous1("python" , 21 )
    Result = Marvellous1("pyhton", 21)
    print("return value is :",Result)
if __name__ == "__main__":
    main()
    

