
def main ():
    size = 0    
    value = 0
    sum = 0 
    size = int(input("Enter the Number of elements:"))

    Data =  list()        
    
    print("enter the data:")                                      
    for i in range (size):
        value = int(input())
        Data.append(value)  #data[i] = vlaue this line can be used but due to the memeory constrain the append is used as it gives to assurity of the data allocation 
    for i in range(size):
        sum = sum + Data[i]
    print("Summation is : ", sum)


if(__name__ == "__main__"):
    main()