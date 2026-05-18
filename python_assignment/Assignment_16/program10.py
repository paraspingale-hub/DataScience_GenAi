def get_name_length(name):
    return len(name)

if __name__ == "__main__":
    user_name = input("Enter name: ")
    length = get_name_length(user_name)
    print("Output:", length)