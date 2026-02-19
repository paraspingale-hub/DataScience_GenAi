def main ():
    ans = 0
    try:
        print("Inside Try")
        No1 = int(input("Enter first nos:"))
        No2 = int(input("Enter second nos:"))    
        ans = No1 / No2 

    except ZeroDivisionError as zobj:
        print("Inside Execept ZOBJ")
    
    except ValueError as vobj:
        print("Inside Execept VOBJ")
    
    except Exception as eobj:
        print("Inside Execept EOBJ")
    
    finally:
        print("Inside Finaly")
    
    
    print("Division is: ", ans)




if __name__ == "__main__":
    main()