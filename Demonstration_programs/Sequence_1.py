value1 =[100,20,30,40]          #list(dublicate) 
print(value1[0])    #10
value1[2] = 35      #change value at pos 
print(value1)

value2 =(100,20,30,40)          #tuple(dublicate)
print(value2[0])    #10
value2[2] = 35
print(value2)                   #error (the value cannot be changed )

value3 ={100,20,30,40}          #set(no dublicate)
print(value3[0])    #error
value3[2] = 35      #error

