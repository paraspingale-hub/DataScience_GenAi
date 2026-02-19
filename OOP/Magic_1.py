#Dunder method \ Magic method \ Special method 
class Demo:
    def __init__(self , A):
        self.no = A
    def __add__(self , other):
        return self.no + other.no
    def __sub__(self , other):
        return self.no - other.no
    def __mul__(self , other):
        return self.no * other.no
    def __truediv__(self , other):
        return self.no / other.no
    
obj1 = Demo(11)
obj2 = Demo(21)

print(11+21)

print(obj1 + obj2)                                  #internal working -> __add__(obj1,obj2) -> obj1 jata self adhe obj2 jata other madhe on line 5 
print(obj1 - obj2)                                  #internal working -> __sub__(obj1,obj2) -> obj1 jata self adhe obj2 jata other madhe on line 7                                  
print(obj1 * obj2)                                  #internal working -> __mul__(obj1,obj2) -> obj1 jata self adhe obj2 jata other madhe on line 9
print(obj1 / obj2)                                  #internal working -> __truediv__(obj1,obj2) -> obj1 jata self adhe obj2 jata other madhe on line 11
