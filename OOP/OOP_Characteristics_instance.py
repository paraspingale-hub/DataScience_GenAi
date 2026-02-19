import gc                                           

class demo :
    #class variable
    no1 = 10
    no2 = 20
    def __init__(self):
        #instance variable 
        self.a = 101
        self.b = 201
    def __del__(self):
        print("Inside Destructor")

print(demo.no1)
print(demo.no2)

obj = demo()

print(obj.a)
print(obj.b)

