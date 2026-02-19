import threading

iCnt = 0

lobj = threading.Lock()                                         # declaring lock as global 

def Update():
    global iCnt
    for _ in range(200000000):
        with lobj:                                              #evrything uder this will be under {only one process will work after the process is completed then only a new process enters 
            iCnt = iCnt + 1
    
def main():
    global iCnt 
    t1 = threading.Thread(target = Update)
    t2 = threading.Thread(target = Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Vlaue of icnt is :",iCnt)
    

if __name__ == "__main__":
    main()