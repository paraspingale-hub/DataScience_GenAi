#polymorphism 

class parent:
    def __init__(self):
        print("INSIDE PARENT CONSTRUCTOR")
    def fun(self):
        print("INSIDE FUN METHOD OF PARENT")
        print(self.no1 , self.no2)

class child(parent):
    def __init__(self):
        super().__init__()
        print("INSIDE CHILD CONSTRUTOR")

        
    def fun(self):
        super().fun()
        print("INSIDE FUN METHOD OF CHILD") 

cobj = child()

cobj.fun()
