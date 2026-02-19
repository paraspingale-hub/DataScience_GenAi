import time
import os
def SumCube(No):
    sum =0
    print("Process is runing with PId:",os.getpid())

    for i in range (1,No+1):
        sum = sum + (i**3)
    return sum
    
    
def main():
    data = [1000000,2000000,3000000,40000000,50000000,6000000,7000000,8000000,9000000,10000000]
    result = []
    starttime = time.time()
    for i in range(len(data)):
        ret = SumCube(data[i])
        result.append(ret)
    print(result)
    endtime = time.time()

    print("Time consumed is:",endtime - starttime)


if __name__ == "__main__":
    main()