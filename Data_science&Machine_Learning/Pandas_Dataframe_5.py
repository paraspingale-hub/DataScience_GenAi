import pandas as pd
def main():
    Dataframe = {
        "Name": ["Paras", "`Piyush", "Pawan", "Pratik"],
        "Age": [21, 22, 23, 24],
        "City": ["Pune", "Mumbai", "Delhi", "Bangalor"]
    }
    dobj = pd.DataFrame(Dataframe)
    
    
    
    print(dobj.loc[:,"Name"]) # Accessing the "Name" column using .loc
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
   