import sys

def main ():
    Border = "-" * 55
    print(Border)
    print("-----------------Marvellous_Automation-----------------")
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H") ):
            print("This application is used to perform --")
            print("This is an automtion script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U") ):
            print("use the given script as")
            print("Scriptname.py Argument1 Argument2")
            print("Argument1 :")
            print("Argument2 :")
        else:
            print("chukla manda")
            print("Use the given flag as:")
            print("--u : ued to display the usage")
            print("--h : ued to display the help")
    else:
        print("invalid no of command line arguments ")
        print("Use the given flag as:")
        print("--u : ued to display the usage")
        print("--h : ued to display the help")

    print(Border)
    print("------------Thank you for using our script ------------")
    print("-----------------Marvellous_Infosystems----------------")
    print(Border)
    
if __name__ == "__main__":
    main()