def display_first_10_even():
    count = 0
    num = 2
    while count < 10:
        print(num, end="   ")
        num += 2
        count += 1
    print()

if __name__ == "__main__":
    display_first_10_even()