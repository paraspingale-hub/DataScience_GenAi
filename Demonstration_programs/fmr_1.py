#filter map reduce
def CheckEven(No):
    return(No % 2 == 0)                         #bool return type 

def main ():
    Data = [11,10,15,20,22,27,30]               #list declaration 
    print("actuall data is :" , Data)
    #filter 
    FData = list(filter(CheckEven , Data))            #function is given as parameter to another function 
                                                      #list madhe typecast kela tela 
    print("Data after filter is : " , FData)    
if(__name__ == "__main__"):
    main()