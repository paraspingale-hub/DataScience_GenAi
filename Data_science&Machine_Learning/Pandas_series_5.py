import pandas as pd
def main():
    data = [11,21,51,101,111]                                   
    print(data)                                                  #display the data as list 
    sobj = pd.Series([25000,27000,29000,30000], index = ['PPA',"LB","Python","React"])  
    print(sobj)
    print(sobj["Python"])  
if __name__ == "__main__":
    main()
    
    
    
    
    
    
   