class node :
    def __init__(self ,vlaue):
        self.data = vlaue
        self.next = None
        

def main ():
    head = None
    
    obj1 = node(11)             #object on node 
    obj2 = node(21)             #object on node 
    obj3 = node(51)             #object on node 
    obj4 = node(101)            #object on node 

    head = obj1
    head.next = obj2
    head.next.next = obj3
    head.next.next.next = obj4
    head.next.next.next.next = None
    
    temp = head
    iCount = 0
    
    while temp is not None:
        print(" | " , temp.data , " |->",end=" ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    main()
    
    
