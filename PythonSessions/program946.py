
def factors(nos):
    fact = 0
    for i in range (1 , nos+1):
        if(nos % i == 0):
            print(i)

def main ():
    ino = int(input("Enter  the nos"))
    factors(ino)
    
        
main()
