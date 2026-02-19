from fmr_Marvellous import FilterX,MapX,ReduceX

CheckEven = lambda No: (No % 2 == 0)
Increament = lambda No:(No + 1)
Add = lambda No1 ,No2:(No1 + No2)
                              
def main ():
    Data = [11,10,15,20,22,27,30]               
    print("actuall data is :" , Data)
    
    #filter 
    FData = list(FilterX(CheckEven , Data))            
    print("Data after filter is : " , FData)    

    #map
    MData = list(MapX(Increament , FData))
    print("Mapping is done :" , MData)   
    
    #reduce
    RData =  ReduceX(Add , MData)                        
    print("DAta after Reduce is: ", RData)

if(__name__ == "__main__"):
    main()