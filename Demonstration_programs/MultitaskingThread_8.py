import threading      
def Display(no):
    print("Inside display",no)
def main():
    t1=threading.Thread(target = Display ,args=(11 ,))                          #it is a tuple and the comma in the last tells that more nos could be added 
    t1.start()


if __name__ == "__main__":
    main()