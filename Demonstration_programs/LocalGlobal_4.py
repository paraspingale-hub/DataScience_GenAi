No = 11                                                         #global , data defination 

def fun ():   
    global No                                             
    print("value of no from Fun function is: ",No)              #11    
    No = No +1                                                  #no = 12  {gloal value change hoti}
    print("value of no from Fun function is: ",No)              #12

print("value of the global no is :" , No)                       #11
fun()                                                           
print("value of the global no is :" , No)                       #12





