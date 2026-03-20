def SmallString(brr):
    smallstr = ""
    for i in range (len(brr)):
        if(brr[i] >= 'a'and brr[i] <= 'z'):
            smallstr = smallstr + brr[i]
    return smallstr
            

def main ():
    print("Enter string")
    
    arr = input()
    ret =  SmallString(arr)
    print("Updated string is :" ,ret)
    
    print(str.lower(arr))
    
    
main()