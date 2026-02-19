#we are performing the rocedualral progeamming in this code
def Addition (a , b):
     return a + b
def Sunctraction (a , b):
     return a - b


NO1 = 0
No2 = 0
No3 = 0

No1 = int(input("Enter first nos "))
No2 = int(input("Enter Sec nos "))
No3 = int(input("Enter Third nos "))

ans = Addition(No1 , No2)
print("Addition is :" , ans)

ans = Sunctraction(No2 , No3)
print("Substraction is :" , ans)
