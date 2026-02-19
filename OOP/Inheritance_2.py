#silgle level
class parent:
    def __init__(self):
        print("iNSIDE PARENT CONSTRUCTOR")
        self.no1 = 10
        self.no2 = 20
    def fun(self):
        print("INSIDE FUN METHOD OF PARENT" , self.no1 , self.no2)
        print(self.no1 , self.no2)

class child(parent):
    def __init__(self):
        super().__init__()
        print("INSIDE CHILD CONSTRUTOR")
        self.A = 11
        self.B = 21
        
    def sun(self):
        print("INSIDE SUN METHOD OF CHILD", self.A , self.B , self.no1 , self.no20
              ) 


cobj = child()


print(cobj.no1)
print(cobj.no2)

print(cobj.A)
print(cobj.B)

cobj.fun()
cobj.sun()

