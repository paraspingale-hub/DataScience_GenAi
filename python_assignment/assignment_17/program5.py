def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
        
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
            
    return True

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    
    if is_prime(number):
        print("Output: It is Prime Number")
    else:
        print("Output: It is not a Prime Number")