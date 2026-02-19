#filter map reduce
def CheckEven(No):
    return(No % 2 == 0)

def main ():
    Data = [11,10,15,20,22,27,30]               #list declaration 
    print("actuall data is :" , Data)
    #filter 
    FData = filter(CheckEven , Data)            #function is given as parameter to another function 
                                                #this will give the place where the Fdata is saved to print the data we typecast it in the list daatype 
    print("Data after filter is : " , FData)    
if(__name__ == "__main__"):
    main()

    #output
#    $ python fmr_1_1.py
#actuall data is : [11, 10, 15, 20, 22, 27, 30]
#Data after filter is :  <filter object at 0x00000208336ab970>
