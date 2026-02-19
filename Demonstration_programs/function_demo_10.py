#onr function can call anaother function 
def  fun ():
    print("Inside Fun")
def gun ():
    print("Inside Gun")
    fun()
def main ():    
    gun()
    
if __name__ == "__main__":
    main()
    

