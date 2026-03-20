def Mimumn(brr):
    max = brr[0]
    for i in range (len(brr)):
        if (brr[i] < max):
            max = brr[i]
    
    return max
                
    return sum 
    
    
def main ():
    size = 0
    arr = []
    
    print("enter no of elemnt")
    size = int(input())
    
    print("Enter the elements : ")
    value = 0
    for i in range (size):
        Value= int(input())
        arr.append(Value)
        
    ret = Mimumn(arr)
    print("Mimumn value  is : " , ret)
    
    

main()



