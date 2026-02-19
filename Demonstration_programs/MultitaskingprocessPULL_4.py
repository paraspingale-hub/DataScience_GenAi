import multiprocessing
import time
def SumCube(No):
    sum =0
    for i in range (1,No+1):
        sum = sum + (i**3)
    return sum
    
    
def main():
    data = [1000000,2000000,3000000,40000000,50000000,6000000,7000000,8000000,9000000,10000000]
    result = []
    starttime = time.time()
    
    pobj = multiprocessing.Pool()
    result = pobj.map(SumCube , data)
    pobj.close()
    pobj.join()
    
    endtime = time.time()



    print("Time consumed is:",endtime - starttime)


if __name__ == "__main__":
    main()