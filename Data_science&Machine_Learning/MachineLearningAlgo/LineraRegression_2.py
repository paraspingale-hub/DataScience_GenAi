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
    
    n = len(x)                  #lenght of the data set
    
    # Y = mX+C
    # m = (sum(x - X_bar)(y - Y_bar)) / (sum(x - X_bar)^2)
    
    numerator = 0
    denominator = 0
    
    for i in range(n):
        numerator = numerator + (x[i] - mean_x) * (y[i] - mean_y)
        denominator = denominator + (x[i] - mean_x) ** 2
    
    m = numerator / denominator
    print(f"Slope of line : {m}")


    c = mean_y - m * mean_x
    print(f"Y intercept of line : {c}")
    
    
    

def main ():
    marvellouspredictor()



if __name__ == "__main__":
    main()