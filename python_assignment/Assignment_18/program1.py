def add_elements(data_list):
    total = 0
    for num in data_list:
        total += num
    return total

if __name__ == "__main__":
    size = int(input("Input : Number of elements : "))
    
    elements = []
    print("Input Elements : ")
    for i in range(size):
        elements.append(int(input()))
        
    result = add_elements(elements)
    print(f"Output : {result}")