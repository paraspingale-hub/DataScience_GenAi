#filter map reduce
def CheckEven(No):
    return(No % 2 == 0)      

def Increament(No):
    return No + 1                    

def main ():
    Data = [11,10,15,20,22,27,30]               
    print("actuall data is :" , Data)
    #filter 
    FData = list(filter(CheckEven , Data))            
    print("Data after filter is : " , FData)    

    #map
    MData = list(map(Increament , FData))
    print("Mapping is done :" , MData)                          #as it is the list datatype (mutable) laterr the internal data can be changed 
if(__name__ == "__main__"):
    main()