import time 
import multiprocessing
import os
def sumeven(no):
    sum = 0
    print("PID of sumeven",os.getpid())
    print("PPID of sumeven :",os.getppid())

    for i in range(2,no+1,2):
        sum = sum + i
    print("EVen sum is :",sum)


def oddsum(no):
    sum = 0
    print("PID of oddsum ",os.getpid())
    print("PPID of oddsum :",os.getppid())
    for i in range(1,no+1,2):

        sum = sum + i
    print("odd sum is :",sum)


def main():
    print("PID of main : ",os.getpid())
    print("PPID of main :",os.getppid())                    ;
    starttime = time.time()

    t1 = multiprocessing.Process(target=sumeven, args=(30000000,))
    t2 = multiprocessing.Process(target=oddsum, args=(30000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    endtime = time.time()
    print("Time taken :", endtime - starttime)


if __name__ == "__main__":
    main()