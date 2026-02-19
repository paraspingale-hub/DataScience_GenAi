#filter map reduce using the lambda functions
from functools import reduce                                

CheckEven = lambda No: (No % 2 == 0)
Increament = lambda No:(No + 1)
Add = lambda No1 ,No2:(No1 + No2)


def main ():
    Data = [11,10,15,20,22,27,30]               
    print("actuall data is :" , Data)
    
    #filter 
    FData = list(filter(CheckEven , Data))            
    print("Data after filter is : " , FData)    

    #map
    MData = list(map(Increament , FData))
    print("Mapping is done :" , MData)   
    
    #reduce
    RData =  reduce(Add , MData)                        
    print("DAta after Reduce is: ", RData)

if(__name__ == "__main__"):
    main()