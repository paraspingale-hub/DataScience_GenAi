import pandas as pd
def main():
    data = [11,21,51,101,111]                                   
    print(data)                                                  #display the data list
    sobj = pd.Series(data)                                       #Series is a one-dimensional array-like object that can hold any data type, such as integers, floats, strings, etc. It is similar to a column in a spreadsheet or a database table.
    print(sobj)
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    # Output:
    # [11, 21, 51, 101, 111]
    # 0     11
    # 1     21
    # 2     51      
    # dtype: int64 