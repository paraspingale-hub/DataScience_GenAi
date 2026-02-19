#we are performing the functional programming in this code
Addition = lambda a , b:  a + b
Sunctraction  = lambda a , b: a - b

NO1 = 0
No2 = 0

No1 = int(input("Enter first nos "))
No2 = int(input("Enter Sec nos "))

ans = Addition(No1 , No2)                               # the control will not go to the line 1 it will bring the bussines logic to the line 12 and perform the bussiness logic 

print("Addition is :" , ans)

ans = Sunctraction(No2 , No1)                           # the control will not go to the line 1 it will bring the bussines logic to the line 12 and perform the bussiness logic 
print("Substraction is :" , ans)