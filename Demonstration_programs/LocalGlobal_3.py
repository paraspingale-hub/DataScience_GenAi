No = 11                                                         #global , data defination 

def fun ():   
    No = 21                                               
    print("value of no from Fun function is: ",No)              #21     
    No = No +1                                                  #no = 22
    print("value of no from Fun function is: ",No)              #22

print("value of the global no is :" , No)                       #11
fun()                                                           
print("value of the global no is :" , No)                       #11





# errror if the line 4 is removed 
#$ python localglobal_3.py
#value of the global no is : 11
#Traceback (most recent call last):
#  File "D:/marvellous_info/python/python_code/demonstration_programs/localglobal
#_3.py", line 9, in <module>
#    fun()
#    ^^^^^
#  File "D:/marvellous_info/python/python_code/demonstration_programs/localglobal
#_3.py", line 4, in fun
#    print("value of no from Fun function is: ",No)              #11
#                                               ^^
#UnboundLocalError: cannot access local variable 'No' where it is not associated
#with a value

