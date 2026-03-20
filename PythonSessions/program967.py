def countcapital(brr):
    icount = 0
    
    for i in range (len(brr)):
        if(brr[i] >= 'A'and brr[i] <= 'Z'):
            icount = icount+1
            
    return icount
    
    
def main ():
    print("Enter string")
    
    arr = input()
    
    print("Enter String is : " ,arr)
    print(len(arr) , "Is the lenght of the string")
    
    ret = countcapital(arr)
    print(ret)
main()



