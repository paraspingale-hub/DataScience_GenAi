import gc                                           

class demo :
    #class variable
    no1 = 10
    no2 = 20
    def __init__(self):
        print("Inside constructor")
    def __del__(self):
        print("Inside Destructor")

print(demo.no1)
print(demo.no2)


