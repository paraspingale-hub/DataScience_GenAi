import threading

iCnt = 0
def Update():
    global iCnt
    for _ in range(200000):
        iCnt = iCnt + 1
    return iCnt
def main ():
    global iCnt
    Update()
    print("Value of icnt is :", iCnt)

    Update()
    print("Value of icnt is :", iCnt)

if __name__ == "__main__":
    main()