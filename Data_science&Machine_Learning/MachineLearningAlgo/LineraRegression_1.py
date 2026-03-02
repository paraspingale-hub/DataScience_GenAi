import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marvellouspredictor():
    #load the data 
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]
    
    print(f"values of independent variable x : {x}")
    print(f"values of independent variable v : {y}")
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    print("Mean of x is: ",mean_x)
    print("Mean of y is: ",mean_y)
    
    

    


def main ():
    marvellouspredictor()



if __name__ == "__main__":
    main()