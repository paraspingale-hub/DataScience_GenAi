class Arithmatic:                                           
    
    def Addition (self ,a , b):                             
     return a + b
    def Sunctraction (self ,a , b):
     return a - b
NO1 = 0
No2 = 0

No1 = int(input("Enter first nos "))
No2 = int(input("Enter Sec nos "))

obj = Arithmatic()


ans = obj.Addition(No1 , No2)
print("Addition is :" , ans)

ans = obj.Sunctraction(No1 , No2)                    
print("Substraction is :" , ans)
