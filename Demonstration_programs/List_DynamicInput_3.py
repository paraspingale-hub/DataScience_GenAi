def summation(Arr):
    sum = 0
    for i in range(len(Arr)):
        sum = sum + Arr[i]
    return sum.as_integer_ratio
    

def main ():   
    value = 0
    ret = 0
    size = int(input("Enter the Number of elements:"))
    Data =  list()        
    
    print("enter the data:")                                      
    for i in range (size):
        value = int(input())
        Data.append(value)  #data[i] = vlaue this line can be used but due to the memeory constrain the append is used as it gives to assurity of the data allocation 
   
    ret = summation(Data)
    print("Summation is :",ret)

if(__name__ == "__main__"):
    main()