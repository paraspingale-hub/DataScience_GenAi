def SmallString(brr):
    smallstr = []
    for i in range (len(brr)):
        if(brr[i] >= 'a'and brr[i] <= 'z'):
            smallstr.append(brr[i])
    print(smallstr)
            

def main ():
    print("Enter string")
    
    arr = input()
    SmallString(arr)
    
main()