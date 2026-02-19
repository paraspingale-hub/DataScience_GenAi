#
#
class Arthmatic:
    def __init__(self , a , b):                                     #parameterised constructor , magic methos
        self.no1 = a 
        self.no2 = b
        print("Object gets created successfully")

    def Addition(self):                                             #instance method 1
        ans = 0
        ans = self.no1 + self.no2
        return ans
    def Substraction(self):                                         #instance method 2
        ans = 0
        ans = self.no1 - self.no2
        return ans
    

obj1 = Arthmatic(11,10)                                             #Internal working --> Arithmatic(id(obj1) , 11, 10 ) -> __init__(obj1) , 11, 10)
obj2 = Arthmatic(21,20)

ret = obj1.Addition()                                               #Internal working --> addition(id(obj1)) -> addiotn gets the address of the obj which contains the data  
print("Addition is :" ,ret)

ret = obj2.Substraction()
print("substration is :" ,ret)