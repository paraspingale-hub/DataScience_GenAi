def check_divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = check_divisible(number)
    print("Output:", result)