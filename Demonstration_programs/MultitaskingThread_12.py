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

    t1 = threading.Thread(target=sumeven, args=(30000000,))
    t2 = threading.Thread(target=oddsum, args=(30000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    endtime = time.time()
    print("Time taken :", endtime - starttime)


if __name__ == "__main__":
    main()