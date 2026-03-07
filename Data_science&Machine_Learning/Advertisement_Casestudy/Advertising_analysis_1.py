import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score


def MarvellousAdvertise(DataPath):
    
    border = "-"*40
    #----------------------------STEP 1 : LOAD DATASET---------------------------------------#
    print(border)
    print("Loading the dataset")
    df = pd.read_csv(DataPath)
    print(border)
    
    print("Few records form the dataset : " )
    print(df.head())
    #----------------------------STEP 2 : REMOVE UNWANTED COLUMS------------------------------#
    
    print(border)
    print("rmove the unwanted coloums ")
    print("Shape of data after cleaaning :" , df.shape)
    if 'unnamed: 0' in df.columns:
        df.drop(columns=['uunamed: 0'] , inplace=true)
        
    print("Shape of data after cleaaning :" , df.shape)
    
    print("Clean data set is : " )
    print(df.head)
    
    print(border)
    
    #--------------------------------STEP 3 : CHECK MISSING VALUES------------------------------#
    
    print(border)
    print("Total missing values : \n")
    print(df.isnull().sum())
    print(border)
    
    

    #--------------------------------STEP 4 : DISPLAY STATISTICAL SUMMATY-------------------------#
    print(border)
    print("Display Statistical summary ")
    print(border)
    print(df.describe())
    
    
    #------------------------STEP 5 : DISPLAY COOREALTIONS BETWEEN COLMS --------------------------#
    
    print(border)
    print("Display coorealtionsbtween the colms ")
    print(border)
    
    print("coorealtion matrix:")
    print(df.corr())
    
    
    





def main():
    MarvellousAdvertise("Advertising.csv")
    
if __name__ == "__main__" :
    main()


