import threading      
def Display(no1,no2,no3):
    print("Inside display",no1,no2,no3)
def main():
    t1=threading.Thread(target = Display ,args=(11 ,21 ,51,))                          #it is a tuple and the comma in the last tells that more nos could be added 
    t1.start()


if __name__ == "__main__":
    main()