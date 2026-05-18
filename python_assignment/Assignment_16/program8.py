def print_stars(num):
    for _ in range(num):
        print("*", end="   ")
    print()

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print_stars(number)