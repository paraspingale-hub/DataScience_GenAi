def calculate_frequency(data_list, target):
    count = 0
    for num in data_list:
        if num == target:
            count += 1
    return count

if __name__ == "__main__":
    size = int(input("Input : Number of elements : "))
    
    elements = []
    print("Input Elements : ")
    for i in range(size):
        elements.append(int(input()))
        
    search_element = int(input("Element to search : "))
    
    result = calculate_frequency(elements, search_element)
    print(f"Output : {result}")