import threading      
import time 
def sumeven(no):
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    print("EVen sum is :",sum) 


def oddsum(no):
    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i
    print("odd sum is :",sum)


def main():
    starttime = time.time()
    sumeven(30000000)
    oddsum(30000000)
    endtime = time.time()
    print("Time taken :", endtime - starttime)


if __name__ == "__main__":
    main()