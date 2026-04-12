import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

def main():
    dobj = pd.DataFrame(
        {
            "A" : [1,2,3],
            "B" : [4,1,6],
            "C" : [7,8,9]
        }
    )
    print(dobj)
    #print(dobj.corr())
    
    #used  to display the correation Feature
    sns.heatmap(dobj.corr(), annot = True)    
    plt.show()
if __name__ == "__main__":
    main()
    
    
    
    
    
    #understand the corr method