import gc 
class demo :
    no = 10
    def __init__(self,a,b):                                    #parameterised constructor
        self.value1 = a
        self.value2 = b
        print("inside the constructor")

print("class variable",demo.no)
obj1 = demo(12 , 23)
obj2 = demo(23 , 34)

print("instance variable of obj1 = " , obj1.value1 , obj1.value2)
print("instance variable of obj2 = " , obj2.value1 , obj2.value2)

