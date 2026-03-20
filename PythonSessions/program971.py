def countcapital(brr):
    icount = 0
    
    for ch in brr:
        if(ch >= 65 and ch <= 90):    #issue
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



