import MarvellousNum

def ListPrime(data_list):
    prime_sum = 0
    for num in data_list:
        # Calling the function from the imported module
        if MarvellousNum.ChkPrime(num):
            prime_sum += num
    return prime_sum

if __name__ == "__main__":
    size = int(input("Input : Number of elements : "))
    
    elements = []
    print("Input Elements : ")
    for i in range(size):
        elements.append(int(input()))
        
    result = ListPrime(elements)
    print(f"Output : {result}")