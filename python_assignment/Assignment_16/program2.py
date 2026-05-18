def ChkNum(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    ChkNum(number)