import pandas as pd
def main():
    Dataframe = {
        "Name": ["Paras", "`Piyush", "Pawan", "Pratik"],
        "Age": [21, 22, 23, 24],
        "City": ["Pune", "Mumbai", "Delhi", "Bangalor"]
    }
    dobj = pd.DataFrame(Dataframe)
    
    # fetching specific row 
    
    print(dobj.loc[1]) # Accessing row with index 1
    print(dobj.loc[0:2]) # Accessing rows from index 0 to 2 (inclusive)
if __name__ == "__main__":
    main()
    
    
    
    
    
    
   