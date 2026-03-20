def Togglecase(brr):
    icount = 0
    result =""
    
    for ch in brr:
        if(ch >= 'A' and ch <= 'Z'): 
            result = result + chr((ord(ch) + 32))
        elif(ch >= 'a' and ch <= 'z'):
            result = result + chr((ord(ch) - 32))
        else:
            result = result + ch
            
    return result
    
    
def main ():
    
    print("Enter string")
    
    arr = input()
    
    print("Enter String is : " ,arr)
    
    print(len(arr) , "Is the lenght of the string")
    
    ret = Togglecase(arr)
    
    print(ret)
    
main()


