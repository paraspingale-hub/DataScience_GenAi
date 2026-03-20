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
    obj1.next = obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = None
    
    

    print(id(obj2))             #address of obj2
    print(id(obj1.next))        #address of obj1.next which is obj2 

    print(obj1.data)
    print(obj1.next.data)
    print(obj1.next.next.data)
    print(obj1.next.next.next.data)
    
if __name__ == "__main__":
    main()
    
    
    
#hardcoded linked list 
#head reff to obj1 which furthur reffers to obj1 -> obj2 -> obj3 ....