def Sum(a):
    sum = 0
    for i in range (0 ,a ):
        sum = sum + i 
        return sum
num = int(input("Enter a number to display its multiplication table: "))
result = Sum(num)
print(f"The sum of numbers from 0 to {num} is: {result}")