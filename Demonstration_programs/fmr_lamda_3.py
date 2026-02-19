#filter map reduce using the lambda functions
from functools import reduce                                

def main ():
    Data = [11,10,15,20,22,27,30]               
    print("actuall data is :" , Data)
    
    #filter 
    FData = list(filter((lambda No: (No % 2 == 0)) , Data))            
    print("Data after filter is : " , FData)    

    #map
    MData = list(map((lambda No:(No + 1)) , FData))
    print("Mapping is done :" , MData)   
    
    #reduce
    RData =  reduce((lambda No1 ,No2:(No1 + No2)) , MData)                        
    print("DAta after Reduce is: ", RData)

if(__name__ == "__main__"):
    main()