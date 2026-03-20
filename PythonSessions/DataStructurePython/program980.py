class Artihmatic : 
    #constructor
    def __init__ (self , a =0 , b =0):
        self.no1 =a #charecteristrics
        self.no2 =b  #charecteristrics
        
    def Addition(self):
        ans = 0
        ans = self.no1 + self.no2
        return ans
    
    def Subtraction (self):
        res = 0
        res = self.no1 - self.no2
        return res 
    
def main ():
    dobj = Artihmatic(11)
    
    ret = dobj.Addition()
    print("Addiotion is. :" ,ret)
    
    ret = dobj.Subtraction()
    print("Subtraction is  :" ,ret)

main()


