def multiplicaiton(vlaue1 , value2):
    mul = 0
    mul = (vlaue1 * value2)  
    return mul 

def main ():

    no1 = 0 
    no2 = 0 
    result = 0 

    no1 = int(input("enter the 1st nos"))
    no2 = int(input("enter the 2nd nos")) 
    result = multiplicaiton(no1 , no2)
    print("Multiplication is :" , result)

#starter point
if __name__ == "__main__" :
    main()
