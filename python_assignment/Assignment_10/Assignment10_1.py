def table(a):
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
num = int(input("Enter a number to display its multiplication table: "))
table(num)