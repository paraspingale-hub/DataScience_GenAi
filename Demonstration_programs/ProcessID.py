#understanding the concept of PID
import os                                                
def main ():
    print("PID of running process is :", os.getpid())
    print("PID of parent process is " , os.getppid())           #parent id which is uusually cmd this value is usvalu constant 

if __name__ == "__main__":
    main()