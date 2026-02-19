import gc                                           #garbage collector 
class demo :
    def __init__(self):
        print("Inside constructor")
    def __del__(self):
        print("Inside Destructor")

obj = demo()
del obj                                             #free or delete in other language similar del in python 
gc.collect()                                        #garbage collector request 
print("End of application")


