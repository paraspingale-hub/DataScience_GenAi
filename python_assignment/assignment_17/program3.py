def calculate_factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0:
        return 1
    
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = calculate_factorial(number)
    print("Output:", result)