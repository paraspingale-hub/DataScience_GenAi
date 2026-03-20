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
    
    
    # creating the linked list <hardcoded>
    head = obj1
    head.next = obj2
    head.next = obj3
    head.next = obj4
    head.next = None
    


cl
    
if __name__ == "__main__":
    main()
    
    
    
#hardcoded linked list 
#head reff to obj1 which furthur reffers to obj1 -> obj2 -> obj3 ....