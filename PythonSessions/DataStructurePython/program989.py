class node :
    def __init__(self ,vlaue):
        self.data = vlaue
        self.next = None
        
class SinglyLL :
    def __init__(self):                             #singlyLL cha construtor 
        self.first = None
        self.iCount = 0 
#---------------------------------------------------------------------------------------------------------------------------------------
    def InsertFirst(self ,value):
        newn = node(value)
        #Linked List is empty 
        if self.first == None:
            self.first = newn
        #Linked list contains atleast one node
        else:
            newn.next = self.first                  # new node updated at the location 1
            self.first = newn
            self.iCount = self.iCount + 1           #update the counter 
#-----------------------------------------------------------------------------------------------------------------------------------------
    #DONE
    def Display(self):
        temp = self.first
        while temp is not None:
            print(" | " , temp.data , " |->",end=" ")
            temp = temp.next
            self.iCount = self.iCount + 1 
#----------------------------------------------------------------------------------------------------------------------------------------
    def Deletefirst(self):
        pass
#----------------------------------------------------------------------------------------------------------------------------------------
    def DeleteLast (self):
        pass 
#----------------------------------------------------------------------------------------------------------------------------------------
    def InsertAtPos(self , value ):
        pass
#---------------------------------------------------------------------------------------------------------------------------------------- 
    def DeleteAtPos(self,value):
        pass
#----------------------------------------------------------------------------------------------------------------------------------------
    def InseertLast(self,value):
        newn = node(value)
        #Linked List is empty 
        if self.first == None:
            self.first = value
            self.first = None
        #Linked list contains atleast one node
        else:
            temp = self.first
            while temp.next is not None:
                newn.next = self.first                  # new node updated at the location 1
                self.first = newn
                
            
            self.iCount = self.iCount + 1           #update the counter 
#----------------------------------------------------------------------------------------------------------------------------------------
    #DONE
    def Count(self):
        return self.iCount
#----------------------------------------------------------------------------------------------------------------------------------------
        
        

def main ():
    sobj = SinglyLL()
    
    
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    print("Elements of linked list are:",sobj.Display())
    print("")
    print("Total no of elements in linked list are" , sobj.Count())
    
    
    sobj.InseertLast(111)
    sobj.InseertLast(121)
    print("Elements of linked list are:",sobj.Display())
    print("")
    print("Total no of elements in linked list are" , sobj.Count())
    
    
    

if __name__ == "__main__":
    main()
    
    
