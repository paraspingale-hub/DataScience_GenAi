
class ArrX:
    def __int__(self , size):
        self.size = size 
        self.arr = [0] * size
    def Accept(self , size):
        print("Enter the elements")
        for i in range(self.size):
            value = int(input())
            self.arr[i] =value 
    def Display(self):
         print("Enter the elements")
         for i in range(self.size):
            print()
    def Summation(self):
        pass
    
    
        

def main():
    aobj = ArrX()
    aobj.Accept(5)
    
if __name__ == "__main__":
    main()