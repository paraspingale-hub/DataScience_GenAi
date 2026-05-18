def find_maximum(data_list):
    if not data_list:
        return None
        
    max_num = data_list[0]
    for num in data_list:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == "__main__":
    size = int(input("Input : Number of elements : "))
    
    elements = []
    print("Input Elements : ")
    for i in range(size):
        elements.append(int(input()))
        
    result = find_maximum(elements)
    print(f"Output : {result}")