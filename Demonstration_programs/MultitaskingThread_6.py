import threading      

def display():
    print("Inside display function:",threading.get_ident())
    for i in range(10):
        print("Inside display",threading.get_ident())


def main():
    print("Inside main :")
    t1=threading.Thread(target=display)
    t1.start()
    
    t2=threading.Thread(target=display)
    t2.start()

    t2.join()
    t1.join()

    print("End of main")



if __name__ == "__main__":
    main()