
def checkperfect(nos):
    fact = 0
    sum = 0
    for i in range (1 , int((nos/2)+1)):
        if(nos % i == 0):
            sum  = sum + i
    
    return sum == nos
            

def main ():
    ino = int(input("Enter  the nos"))

    
    sumation = checkperfect(ino)
    
    if(sumation == True):
        print("It is a perfect nos ")
    else:
        print("Not a perfect nos ")c
    
        
main()
