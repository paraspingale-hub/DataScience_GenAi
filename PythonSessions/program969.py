def countsmall(brr):
    icount = 0
    
    for i in range (len(brr)):
        if(brr[i] >= 'a'and brr[i] <= 'z'):
            icount = icount+1
            
    return icount
    
    
def main ():
    print("Enter string")
    
    arr = input()
    
    
    
    ret = countsmall(arr)
    print(ret)
main()



