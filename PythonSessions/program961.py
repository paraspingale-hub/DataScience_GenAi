def Summation(brr):
    sum = 0
    for no in brr:
        sum = sum + no 
    
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
        
    ret = Summation(arr)
    print("Addiotion is : " , ret)
    
    

main()



