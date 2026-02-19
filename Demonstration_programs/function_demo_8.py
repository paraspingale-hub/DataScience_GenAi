# Accept: Multi Parameters
# Return: Multi Parameters
def Marvellous1(Value1 ,Value2):  #positional argument
    print("Inside MArvellous1:" , Value1 , Value2)
    return 11 , 21, 51 
def main (): 
    Result1 = None 
    Result2 = None
    Result3 = None
    Marvellous1("python" , 21 )
    Result1 , Result2 , Result3 = Marvellous1("pyhton", 21)
    print("return value are :",Result1 , Result2 , Result3)
if __name__ == "__main__":
    main()
    

