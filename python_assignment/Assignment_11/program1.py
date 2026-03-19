def checkprime(n):
    if n <= 1:
        print("Non prime nos")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Non prime nos")
            return
    print("Prime nos")
    
if __name__ == "__main__":
    checkprime(11)