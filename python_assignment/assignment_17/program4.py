def sum_of_factors(num):
    if num <= 0:
        return 0
        
    factor_sum = 0
    # We only need to check up to half of the number
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            factor_sum += i
            
    return factor_sum

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = sum_of_factors(number)
    print("Output:", result)