class demo :
    no =10
    def __init__(self,a,b):
        self.Value1 = a
        self.Value2 = b

    def fun(self):
        print("Inside the class method fun" ,self.Value2 ,self.Value1)

    @classmethod    
    def sum (cls):
        print("inside the class method sun",cls.no)

demo.sum()
print("Class variable no :" , demo.no)

obj=demo(11,21)

obj.fun()
print("instance variable :" , obj.Value1 , obj.Value2)

