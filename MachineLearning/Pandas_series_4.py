import pandas as pd
def main():
    data = [11,21,51,101,111]                                   
    print(data)                                                  #display the data as list 
    sobj = pd.Series([11.4,21.45,51.4,101.4,111.4], index = [5,6,7,8,9])  # you can also specify the index of the series using the index parameter. If you do not specify an index, pandas will create a default index starting from 0.                       
    print(sobj)
if __name__ == "__main__":
    main()
    
    
    
    
    
    
   