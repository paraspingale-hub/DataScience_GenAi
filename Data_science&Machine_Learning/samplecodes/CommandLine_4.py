import sys
#$ python CommandLine_3.py 11 10

def main ():
    print("Command Line Arguments are :")
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])
    sum = no1 +no2
    print(sum)                  

if __name__ == "__main__":
    main()