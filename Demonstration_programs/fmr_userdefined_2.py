#filter map reduce using the lambda functions
from functools import reduce                                

CheckEven = lambda No: (No % 2 == 0)
Increament = lambda No:(No + 1)
Add = lambda No1 ,No2:(No1 + No2)



def FilterX(Task , Elements):
    result = list()                 #result = [] can aslo be used
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            result.append(no)
    return result

def MapX(task , elements):
    result = list()
    for no in elements:
        result.append(task(no))                     #shorter form if task(no)is true then it will append in the result else kay nahi honarr 
    return result


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
    RData =  reduce(Add , MData)                        
    print("DAta after Reduce is: ", RData)

if(__name__ == "__main__"):
    main()