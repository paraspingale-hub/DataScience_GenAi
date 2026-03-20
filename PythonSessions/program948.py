
def sumfactors(nos):
    fact = 0
    sum = 0
    for i in range (1 , int((nos/2)+1)):
        if(nos % i == 0):
            sum  = sum + i
    
    if(sum == nos):
        print("It is an perfect nos ")
    else:
        print("Not an perfect nos ")
            

def main ():
    ino = int(input("Enter  the nos"))
    sumfactors(ino)
    
        
main()
