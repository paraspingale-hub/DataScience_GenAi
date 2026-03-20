def Lowercase(brr):
    icount = 0
    
    for ch in brr:
        if(ch >= 'a' and ch <= 'Z'): 
            result = result + chr((ord(ch)+32))
        else:
            result = result + ch
    return icount
    
    
def main ():
    
    print("Enter string")
    
    arr = input()
    
    print("Enter String is : " ,arr)
    
    print(len(arr) , "Is the lenght of the string")
    
    ret = Lowercase(arr)
    
    print(ret)
    
main()



