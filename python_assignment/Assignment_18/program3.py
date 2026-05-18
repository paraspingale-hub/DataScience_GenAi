def find_minimum(data_list):
    if not data_list:
        return None
        
    min_num = data_list[0]
    for num in data_list:
        if num < min_num:
            min_num = num
    return min_num

if __name__ == "__main__":
    size = int(input("Input : Number of elements : "))
    
    elements = []
    print("Input Elements : ")
    for i in range(size):
        elements.append(int(input()))
        
    result = find_minimum(elements)
    print(f"Output : {result}")