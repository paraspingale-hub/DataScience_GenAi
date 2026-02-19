#filter map reduce using user defined functions 
                              

CheckEven = lambda No: (No % 2 == 0)
Increament = lambda No:(No + 1)
Add = lambda No1 ,No2:(No1 + No2)



def FilterX(Task , Elements):
    result = list()                 
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            result.append(no)
    return result

def MapX(task , elements):
    result = list()
    for no in elements:
        result.append(task(no))                     
    return result

def ReduceX(task , elements):
    sum = 0 
    #[11, 21, 23, 31]
    for no in elements:
        sum = task(sum ,no)
    return sum 




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