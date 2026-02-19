class Arithmatic:                                           #class is considers as a root datatype 7777777777777777777772
    
    def Addition (self ,a , b):                             # self is actually this keyword
     return a + b
    def Sunctraction (self ,a , b):
     return a - b
NO1 = 0
No2 = 0

No1 = int(input("Enter first nos "))
No2 = int(input("Enter Sec nos "))


ans = Arithmatic().Addition(No1 , No2)
print("Addition is :" , ans)

ans = Arithmatic().Sunctraction(No1 , No2)                    
print("Substraction is :" , ans)
