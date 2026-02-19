

def main ():
    size = 0    
    value = 0
    size = int(input("Enter the Number of elements:"))

    Data =  list()        
    
    print("enter the data:")                                      
    for i in range (size):
        value = int(input())
        Data.append(value)
    print(Data) 

if(__name__ == "__main__"):
    main()