class node :
    def __init__(self ,vlaue):
        self.data = vlaue
        self.next = None
        
class SinglyLL :
    def __init__(self):                             #singlyLL cha construtor 
        self.first = None
        self.iCount = 0 
#---------------------------------------------------------------------------------------------------------------------------------------
    #DONE
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
    #DONE
    def Deletefirst(self):
        if(self.first == None):                         # u cna also use iCount == 0 then return 
            return
        else:
            temp = self.first
            self.first = self.first.next
            del temp
            self.iCount = self.iCount - 1
#----------------------------------------------------------------------------------------------------------------------------------------
    def DeleteLast (self):
        pass 
#----------------------------------------------------------------------------------------------------------------------------------------
    def InsertAtPos(self , value , pos):
        if(pos < 1 or pos > (self.iCount+1)):
            print("Invalide position")
            return
        if (pos == 1):
            self.InseertLast(value)
            return
        elif(pos == self.iCount+1):
            self.InseertLast(value)
            return
        else:
            newn = node(value)
            temp = self.first
            for i in range (1 , pos-1):
                temp = temp.next
                
            newn.next = temp.next
            temp.next = newn
            self.iCount = self.iCount + 1 
#---------------------------------------------------------------------------------------------------------------------------------------- 
    def DeleteAtPos(self,value ,pos):
        pass
#----------------------------------------------------------------------------------------------------------------------------------------
    def InseertLast(self,value):
        newn = node(value)
        #Linked List is empty 
        if self.first == None:
            self.first = newn
        #Linked list contains atleast one node
        else:
            temp = self.first
            while temp.next is not None:
                newn.next = self.first                  # new node updated at the location 1
                temp.next = newn
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
    
    sobj.InsertAtPos(105 , 4)
    print("Elements of linked list are:",sobj.Display())
    print("")
    print("Total no of elements in linked list are" , sobj.Count())
    
    sobj.Deletefirst()
    sobj.Deletefirst()
    print("Elements of linked list are:",sobj.Display())
    print("")
    print("Total no of elements in linked list are" , sobj.Count())
    
    
    
    
    

if __name__ == "__main__":
    main()
    
    
