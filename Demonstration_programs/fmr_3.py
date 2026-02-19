#filter map reduce
from functools import reduce                                #reduce is imported from an inbuild module named as functools 
def CheckEven(No):
    return(No % 2 == 0)      

def Increament(No):
    return No + 1   
def Add(No1 ,No2):
    return No1 + No2    

             

def main ():
    Data = [11,10,15,20,22,27,30]               
    print("actuall data is :" , Data)
    #filter 
    FData = list(filter(CheckEven , Data))            
    print("Data after filter is : " , FData)    

    #map
    MData = list(map(Increament , FData))
    print("Mapping is done :" , MData)   #as it is the list datatype (mutable) laterr the internal data can be changed
    
    #reduce
    RData =  reduce(Add , MData)                        #reduce is not defined in the python inbuild functions 
    print("DAta after Reduce is: ", RData)


if(__name__ == "__main__"):
    main()