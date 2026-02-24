import sys
#$ python CommandLine_3.py 11 10

def main ():
    print("Command Line Arguments are :")
    sum  = 0
    for i in range(len(sys.argv)):
        no = int(sys.argv[i])
        sum = sum + no
        print(sum)                  

if __name__ == "__main__":
    main()


,,,